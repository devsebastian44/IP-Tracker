# IP-Tracker: Advanced Target Information Gatherer

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI%2FCD-2088FF?style=flat&logo=github-actions&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen)
![OSINT](https://img.shields.io/badge/Type-OSINT-informational)

---

## 🎯 Project Overview

**IP-Tracker** is a programmatic OSINT tool specialized in tracking, geolocating, and enriching data from IPv4 addresses and associated phone information. 

Developed for security analysts and technical consultants, the tool enables:
- Mass resolution and enrichment of network addresses.
- Agile queries during `Footprinting` processes in early stages of Pentesting.
- Integration into detection and manual collection flows.

> [!WARNING]
> **Ethical Disclaimer**: This project is for educational and ethical cybersecurity purposes only. The author is not responsible for any misuse of this tool.

---

## 🏛️ Repository Architecture

This repository is structured under **DevSecOps** standards, ensuring modularity and secure integration:

```
IP-Tracker/
├── src/                  # Core source code
├── scripts/              # Utility scripts
├── tests/                # Unit and integration tests
├── .github/              # GitHub Actions CI/CD pipelines
├── docs/                 # Additional technical documentation
├── diagrams/             # Architectural diagrams (Mermaid)
├── .gitignore            # Exclusion filters
├── LICENSE               # MIT License
└── README.md             # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or superior.
- Recommended OS: Linux (Kali, Parrot, Ubuntu) or Windows with PowerShell.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Devsebastian44/IP-Tracker.git
   cd IP-Tracker
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Execution
Run the main script:
```bash
python src/tracker.py
```

---

## 🧪 Testing

The project includes a suite of unit tests using `pytest` and `unittest` with mocks to ensure stability without needing external API access.

To run tests:
1. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```
2. Execute tests:
   ```bash
   pytest tests/
   ```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:
1. **Fork** the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes using **Conventional Commits**.
4. **Push** to the branch (`git push origin feature/your-feature`).
5. Open a **Pull Request**.

---

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

