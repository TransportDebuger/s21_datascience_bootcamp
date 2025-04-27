import pytest
import requests
from financial import fetch_financial_page, parse_financial_data, get_financial_data

# Test data template
VALID_HTML = '''
<div class="row yf-1yyu1pc"><div class="sticky column yf-1yyu1pc">Breakdown</div> <div class="column yf-1yyu1pc alt" data-cpos="0">TTM </div><div class="column yf-1yyu1pc" data-cpos="1">6/30/2024 </div><div class="column yf-1yyu1pc alt" data-cpos="2">6/30/2023 </div><div class="column yf-1yyu1pc" data-cpos="3">6/30/2022 </div><div class="column yf-1yyu1pc alt" data-cpos="4">6/30/2021 </div> </div>
<div class="row lv-0 yf-t22klz"><div class="column sticky yf-t22klz"><button aria-label="Total Revenue" class="icon-btn fin-size-small tw-p-0 rounded yf-9i625" data-ylk="elm:expand;elmt:btn;itc:1;sec:qsp-financials;slk:TotalRevenue"> <div aria-hidden="true" class="icon fin-icon primary-icn sz-medium yf-9qlxtu"><!-- HTML_TAG_START --><svg viewbox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M16.59 8.59 12 13.17 7.41 8.59 6 10l6 6 6-6z"></path></svg><!-- HTML_TAG_END --></div></button> <div class="rowTitle yf-t22klz" title="Total Revenue">Total Revenue</div></div> <div class="column yf-t22klz alt">261,802,000 </div><div class="column yf-t22klz">245,122,000 </div><div class="column yf-t22klz alt">211,915,000 </div><div class="column yf-t22klz">198,270,000 </div><div class="column yf-t22klz alt">168,088,000 </div></div>
'''

def test_valid_parse(monkeypatch):
    """Test parsing with valid field"""
    result = parse_financial_data(VALID_HTML, 'Total Revenue')
    assert isinstance(result, tuple)
    assert result == ('Total Revenue', '261,802,000', '245,122,000', '211,915,000', '198,270,000', '168,088,000')

def test_invalid_field_parse():
    """Test parsing with invalid field"""
    with pytest.raises(Exception):
        parse_financial_data(VALID_HTML, 'Invalid Field')

def test_network_error(monkeypatch):
    """Test invalid ticker handling"""
    def mock_get(*args, **kwargs):
        raise requests.exceptions.HTTPError
    
    monkeypatch.setattr(requests, 'get', mock_get)
    with pytest.raises(Exception):
        fetch_financial_page('INVALID_TICKER')

def test_full_workflow(monkeypatch):
    
    result = get_financial_data('MSFT', 'Total Revenue')
    
    assert isinstance(result, tuple)
    assert len(result) == 6
    assert all(isinstance(x, str) for x in result)
