import logging
import time
import requests
from random import randint
import config

class MillisecondFormatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        ct = self.converter(record.created)
        t = time.strftime("%Y-%m-%d %H:%M:%S", ct)
        return f"{t},{int(record.msecs):03d}"

logger = logging.getLogger()
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('analytics.log')
formatter = MillisecondFormatter(fmt='%(asctime)s %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class Research:
    def __init__(self, file_path):
        self.file_path = file_path
        logging.info(f"Initialized Research with file: {file_path}")

    def file_reader(self, has_header=True):
        logging.info(f"Reading file {self.file_path} with header={has_header}")
        try:
            with open(self.file_path, 'r') as f:
                lines = [line.strip() for line in f if line.strip()]
            logging.info(f"Successfully read {len(lines)} lines from file")
        except IOError as e:
            logging.error(f"File read error: {e}")
            raise IOError(f"Could not read file: {e}")

        if has_header:
            if len(lines) < 2:
                error_msg = "Not enough lines: header + data required"
                logging.error(error_msg)
                raise ValueError(error_msg)
            header = lines[0].split(',')
            if len(header) != 2 or not header[0] or not header[1]:
                error_msg = "Invalid header format"
                logging.error(error_msg)
                raise ValueError(error_msg)
            data_lines = lines[1:]
            logging.info("Header validated successfully")
        else:
            data_lines = lines

        data = []
        for line in data_lines:
            parts = line.split(',')
            if len(parts) != 2:
                error_msg = f"Invalid line format: {line}"
                logging.error(error_msg)
                raise ValueError(error_msg)
            try:
                a, b = int(parts[0]), int(parts[1])
            except ValueError:
                error_msg = f"Invalid integer values in line: {line}"
                logging.error(error_msg)
                raise ValueError(error_msg)
            if a not in (0, 1) or b not in (0, 1) or a == b:
                error_msg = f"Invalid values in line: {line}"
                logging.error(error_msg)
                raise ValueError(error_msg)
            data.append([a, b])
        logging.info(f"Processed {len(data)} valid data rows")
        return data

    @staticmethod
    def send_telegram_notification(success):
        message = "The report has been successfully created" if success else "The report hasn’t been created due to an error"
        logging.info(f"Attempting to send Telegram notification: {message}")
        try:
            url = f"https://api.telegram.org/bot{config.TELEGRAM_TOKEN}/sendMessage"
            data = {'chat_id': config.TELEGRAM_CHAT_ID, 'text': message}
            response = requests.post(url, data=data)
            response.raise_for_status()
            logging.info("Telegram notification sent successfully")
        except Exception as e:
            logging.error(f"Failed to send Telegram notification: {e}")

    class Calculations:
        def __init__(self, data):
            self.data = data
            logging.info("Initialized Calculations with data")

        def counts(self):
            logging.info("Calculating counts of heads and tails")
            heads = sum(row[0] for row in self.data)
            tails = sum(row[1] for row in self.data)
            logging.info(f"Counts calculated - Heads: {heads}, Tails: {tails}")
            return (heads, tails)
        
        def fractions(self):
            logging.info("Calculating fractions")
            heads, tails = self.counts()
            total = heads + tails
            head_percent = heads / total * 100
            tail_percent = tails / total * 100
            logging.info(f"Fractions calculated - Heads: {head_percent}%, Tails: {tail_percent}%")
            return (head_percent, tail_percent)

class Analytics(Research.Calculations):
    def predict_random(self, num_predictions):
        logging.info(f"Generating {num_predictions} random predictions")
        predictions = [[randint(0, 1), randint(0, 1)] for _ in range(num_predictions)]
        valid_predictions = []
        for pred in predictions:
            if pred[0] == pred[1]:
                pred = [pred[0], 1 - pred[0]]
            valid_predictions.append(pred)
        logging.info(f"Generated {len(valid_predictions)} valid predictions")
        return valid_predictions

    def predict_last(self):
        logging.info("Retrieving last prediction")
        return self.data[-1] if self.data else []

    def save_file(self, data, filename, extension='txt'):
        full_name = f"{filename}.{extension}"
        logging.info(f"Saving data to {full_name}")
        with open(full_name, 'w') as f:
            f.write(str(data))
        logging.info(f"Data successfully saved to {full_name}")