# Free APIs That Need No Key — 30+ Public APIs for Developers (2026)

A curated list of **free, public APIs that require no authentication** — no API key, no OAuth, no signup. Just send a request and get data.

Perfect for prototyping, learning, hackathons, and building MVPs without worrying about rate limits or billing.

> **Need custom data extraction?** I build web scrapers and data pipelines. [See my work](https://github.com/spinov001-art/awesome-web-scraping-2026) or [hire me](https://spinov001-art.github.io).

## Data & Finance

| API | What You Get | Endpoint |
|-----|-------------|----------|
| **CoinGecko** | Crypto prices, 10K+ coins, market data | `api.coingecko.com/api/v3/` |
| **Exchange Rates** | Currency exchange rates, 170+ currencies | `open.er-api.com/v6/latest/USD` |
| **World Bank** | GDP, population, economic indicators | `api.worldbank.org/v2/` |

## Weather & Geo

| API | What You Get | Endpoint |
|-----|-------------|----------|
| **Open-Meteo** | Weather forecast, 16 days, hourly | `api.open-meteo.com/v1/forecast` |
| **ip-api** | IP geolocation, ISP, VPN detection | `ip-api.com/json/` |
| **Countries REST** | Country data — flag, population, capital | `restcountries.com/v3.1/all` |
| **Nominatim (OSM)** | Geocoding — address to coordinates | `nominatim.openstreetmap.org/search` |

## Developer Tools

| API | What You Get | Endpoint |
|-----|-------------|----------|
| **npm Registry** | Package metadata, downloads, versions | `registry.npmjs.org/{package}` |
| **PyPI** | Python package data | `pypi.org/pypi/{package}/json` |
| **GitHub** | Public repos, users, commits | `api.github.com/` |
| **HN Algolia** | Hacker News stories, comments, search | `hn.algolia.com/api/v1/` |

## Knowledge & Research

| API | What You Get | Endpoint |
|-----|-------------|----------|
| **Open Library** | 20M+ books — search by title, ISBN, author | `openlibrary.org/search.json` |
| **arXiv** | 2M+ research papers, full metadata | `export.arxiv.org/api/query` |
| **Wikipedia** | Article content, search, random | `en.wikipedia.org/w/api.php` |
| **Crossref** | 130M+ scholarly articles, DOI lookup | `api.crossref.org/works` |

## DNS & Security

| API | What You Get | Endpoint |
|-----|-------------|----------|
| **Google DNS** | DNS lookups over HTTPS | `dns.google/resolve` |
| **RDAP/IANA** | Domain WHOIS replacement | `data.iana.org/rdap/dns.json` |
| **Shodan InternetDB** | Open ports, vulnerabilities by IP | `internetdb.shodan.io/{ip}` |
| **Have I Been Pwned** | Breached password check (k-anonymity) | `api.pwnedpasswords.com/range/{hash}` |

## Media & Content

| API | What You Get | Endpoint |
|-----|-------------|----------|
| **YouTube Innertube** | Video data, comments, transcripts (no key!) | `youtube.com/youtubei/v1/` |
| **Unsplash** | High-quality stock photos | `source.unsplash.com/random` |
| **Lorem Picsum** | Random placeholder images | `picsum.photos/200/300` |
| **Quotable** | Random quotes | `api.quotable.io/random` |

## Internet Archive

| API | What You Get | Endpoint |
|-----|-------------|----------|
| **Wayback Machine** | Historical snapshots of any website | `archive.org/wayback/available` |
| **Internet Archive** | Books, audio, video, software | `archive.org/metadata/{id}` |

## Government & Open Data

| API | What You Get | Endpoint |
|-----|-------------|----------|
| **USA.gov Data** | Federal datasets | `api.data.gov/` |
| **UK Parliament** | Bills, votes, members | `members-api.parliament.uk/api/` |
| **EU Open Data** | EU statistics and datasets | `data.europa.eu/api/hub/search/` |

## Quick Start

### Python

```python
import requests

# Bitcoin price
btc = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd").json()
print(f"Bitcoin: ${btc['bitcoin']['usd']:,.0f}")

# Weather in NYC
weather = requests.get("https://api.open-meteo.com/v1/forecast?latitude=40.71&longitude=-74.01&current_weather=true").json()
print(f"NYC: {weather['current_weather']['temperature']}C")

# Search arXiv papers
papers = requests.get("https://export.arxiv.org/api/query?search_query=all:RAG+retrieval&max_results=5").text
print(papers[:500])
```

### JavaScript

```javascript
// IP geolocation
const geo = await fetch("http://ip-api.com/json/").then(r => r.json());
console.log(`You are in ${geo.city}, ${geo.country}`);

// npm package info
const pkg = await fetch("https://registry.npmjs.org/express").then(r => r.json());
console.log(`Express latest: ${pkg["dist-tags"].latest}`);
```

## Related Projects

- [awesome-web-scraping-2026](https://github.com/spinov001-art/awesome-web-scraping-2026) — 77 free web scraping tools
- [youtube-rag-knowledge-base](https://github.com/spinov001-art/youtube-rag-knowledge-base) — AI knowledge base from YouTube
- [YouTube Innertube API Tutorial](https://dev.to/0012303/youtube-has-a-hidden-api-that-needs-no-api-key-here-is-how-to-use-it-2n9e)

## Contributing

Know a free API with no key required? Open an issue or PR!

## License

MIT
