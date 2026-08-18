# News sentiment API

News tone over time via the Trends API. Sentiment history and growth without scraping outlets.

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![PyPI](https://img.shields.io/pypi/v/trendsapi-news-sentiment.svg)](https://pypi.org/project/trendsapi-news-sentiment/)

Key: [trendsapi.ai/#get-key](https://trendsapi.ai/#get-key). Full contract: [trendsapi-ai/trendsapi](https://github.com/trendsapi-ai/trendsapi).

## Install

```bash
pip install trendsapi-news-sentiment
```

```python
from trendsapi_news_sentiment import TrendsAPI

client = TrendsAPI()  # TRENDSAPI_KEY
series = client.get_time_series("nvidia")
growth = client.get_growth("nvidia", percent_growth=["12M"])
```

Keyword helpers default to `source: "news sentiment"`. Override `source=` for any other platform. Official full client: [`trendsapi`](https://pypi.org/project/trendsapi/).

## Call

| Field | Value |
|---|---|
| Endpoint | `POST https://api.trendsapi.ai/api` |
| Auth | `Authorization: Bearer $TRENDSAPI_KEY` |
| History | `source: news sentiment` with `get_time_series` or `get_growth` |
| Keyword | Any phrase, e.g. nvidia |
| Live `type` | n/a |

```bash
curl -sS -X POST https://api.trendsapi.ai/api \
  -H "Authorization: Bearer $TRENDSAPI_KEY" \
  -H "Content-Type: application/json" \
  --max-time 60 \
  -d '{"mode":"get_time_series","source":"news sentiment","keyword":"nvidia"}'
```

Negative `growth` means tone fell vs the prior window, not that the company is negative.

Mention count is `news-trends-api` (`source: news volume`).

No per-article labels, no outlet breakdown.

Site: [https://trendsapi.ai/trends/news-sentiment](https://trendsapi.ai/trends/news-sentiment). GitHub: [trendsapi-ai/news-sentiment-api](https://github.com/trendsapi-ai/news-sentiment-api).

## License

MIT. See [LICENSE](LICENSE).
