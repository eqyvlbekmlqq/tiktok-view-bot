# Security Policy

## Scope

tiktok-view-bot is an educational tool that simulates view traffic against
public TikTok video URLs. It does **not** bypass authentication, and it does
not scrape private data.

## Reporting a vulnerability

If you find a security issue (session leakage, proxy credential exposure,
unsafe deserialization in the state store), please email
`security@tiktok-view-bot.dev` with a description and reproduction steps.
Do not open a public issue for security problems.

## Known limitations

- Session cookies are stored in `data/` — this directory is gitignored by
  default. Never commit real session files.
- Proxy lists must be supplied by the user. The bundled
  `data/proxies.example.txt` contains placeholder values only.

## Use at your own risk

Running this bot against accounts or videos you do not own may violate
TikTok's Terms of Service. The maintainers assume no responsibility for
misuse.