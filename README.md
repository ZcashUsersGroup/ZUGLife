# ZDA Project Dashboard

A simple interactive frontend that displays Zcash-related projects from the ZDA Funding API. The page is fully client-side and dynamically pulls grant/project data including funding progress, descriptions, milestones, and contributor information.

## Features

- 🧾 **Dynamic data loading** from the ZDA Funding API (`https://zdafunding-api.onrender.com/api/v1/cards`)
- 🎯 **Sort** projects by checkpoints or alphabetically using a custom dropdown
- 🔍 **Search** projects by **title** and **tags**
- 💰 **Toggle currency display** between ZEC and USD
- 📊 **Progress bars** with milestone checkpoints
- 🔎 **Details modal** with full project description, tags, priority, and milestone status
- 💸 **Contribute modal** showing wallet addresses
- 📈 **Stats panel** for Total Requested, Total Received, and Available Funds

## Demo

> The project is currently designed to be opened directly in a web browser from a local file or hosted statically (e.g., GitHub Pages, Netlify, Vercel).

## Getting Started

1. Clone or download this repository.
2. Open `ZDAweb.html` in any modern browser.
3. Ensure you have internet access to fetch data from the API.

### File Structure

```
ZDAweb.html       # Main HTML file with embedded CSS and JS
README.md        # This file
```

## API Integration

This frontend fetches data from:

```
https://zdafunding-api.onrender.com/api/v1/cards
```

The response includes:

- Project `title`, `description`, `tags`, `milestones`, `priority`
- Funding info: `funding_requested`, `funding_received`, `funding_available`
- Metadata: `contributors`, `date`, `status`, `wallet_addresses`

## Customization

- To change styling, edit the embedded `<style>` block in `ZDAweb.html`.
- To extend functionality (e.g., QR code rendering), update the JavaScript section at the bottom of the HTML.

## Future Improvements

- ✅ Add real QR codes from wallet addresses
- ✅ Highlight matching search results
- 🔲 Add roadmap interactivity
- 🔲 Support pagination from the API

---

### Contact

Built by Jax Feinstein of the ZDA team.  
📧 [zda@proton.me](mailto:zda@proton.me)  
🔗 [GitHub](#) (placeholder)  
🧾 [Transparency / Milestone Archive](#) (placeholder)
