# News sentiment API

Tone over time (`source: news sentiment`). Mention count is [news-trends-api](https://github.com/trendsapi-ai/news-trends-api) (`news volume`).

Key: [trendsapi.ai/#get-key](https://trendsapi.ai/#get-key). Contract: [trendsapi-ai/trendsapi](https://github.com/trendsapi-ai/trendsapi).

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Source](https://img.shields.io/badge/source-news%20sentiment-purple.svg)](https://trendsapi.ai/trends/news-sentiment)

## Call

| Field | Value |
|---|---|
| Endpoint | `POST https://api.trendsapi.ai/api` |
| Auth | `Authorization: Bearer $TRENDSAPI_KEY` |
| History | `source: news sentiment` with `get_time_series` or `get_growth` |
| Keyword | Any phrase, e.g. `nvidia` |
| Live feed | None for tone. Headlines: `type: Google News Top News` |

```bash
curl -sS -X POST https://api.trendsapi.ai/api \
  -H "Authorization: Bearer $TRENDSAPI_KEY" \
  -H "Content-Type: application/json" \
  --max-time 60 \
  -d '{"mode":"get_growth","source":"news sentiment","keyword":"nvidia","percent_growth":["3M","12M"]}'
```

Negative `growth` means tone fell vs the prior window, not that the company "is negative." `value` is a series index, not a per-article probability.

No per-article labels, no outlet breakdown, no model card.

Site: [trendsapi.ai/trends/news-sentiment](https://trendsapi.ai/trends/news-sentiment).

## License

MIT. See [LICENSE](LICENSE).
