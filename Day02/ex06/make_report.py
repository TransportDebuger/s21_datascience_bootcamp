from analytics import Research, Analytics
import config

def generate_report():
    try:
        research = Research(config.csv_file)
        data = research.file_reader()
        analytics = Analytics(data)
        
        heads, tails = analytics.counts()
        head_percent, tail_percent = analytics.fractions()
        
        predictions = analytics.predict_random(config.num_steps)
        next_heads = sum(p[0] for p in predictions)
        next_tails = sum(p[1] for p in predictions)
        
        report_content = config.report_template.format(
            observations=len(data),
            tails=tails,
            heads=heads,
            tail_percent=tail_percent,
            head_percent=head_percent,
            num_steps=config.num_steps,
            next_tails=next_tails,
            next_heads=next_heads
        )
        
        analytics.save_file(report_content, 'report', 'txt')
        Research.send_telegram_notification(True)
        print("Report generated and notification sent successfully")
    except Exception as e:
        Research.send_telegram_notification(False)
        print(f"Error generating report: {e}")

if __name__ == '__main__':
    generate_report()