# Alt-Text Generator

## Goals

Basics

- Drag and drop an image into an interface
- File select as fallback
- Quickly generate alt-text
- One-click copy to clipboard
- Formats: JPEG, PNG

Extra

- Character count in output UI
- History of alt-text generated (cached)
- Length options: concise, default, verbose
- Style options: formal vs casual
- Formats: GIF, WebP
- Paste an image (not image url) as input
- Smooth handling of large images: compress before upload or graceful error handling

Maybe?

- Accounts?
- Editing the output?
- Batch processing?
- URL input

## Stack / Architecture / Design

- Webapp because it's easy
- API call to OpenAI
- Handle everything on client-side
- Store recent history as a cookie
- Next.js on Vercel (hobby tier)
- GitHub actions for CI/CD
- Containerize the development environment if we get around to it (for practice)
- Use TS from the start

## Links / Resources

- [GitHub search for similar projects (post 2024)](https://github.com/search?q=alt+text+generator+pushed%3A%3E2024-01-01+&type=repositories)
- [Vercel "Hobby" plan details](https://vercel.com/docs/accounts/plans/hobby)

