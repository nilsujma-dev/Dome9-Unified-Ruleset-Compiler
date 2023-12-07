## Dome9 Compliance Ruleset Management Scripts

This GitHub repository features two Python scripts designed to interact with Dome9's API for managing custom compliance rulesets. These scripts enable users to extract, process, and submit custom rulesets specific to AWS, Azure, and GCP in the Dome9 platform, facilitating enhanced cloud security and compliance.

### First Script: Ruleset Extraction and Processing
- **Environment Variable Checks**: Ensures that Dome9 credentials are set as environment variables.
- **API Call to Dome9**: Fetches existing compliance rulesets from Dome9's API.
- **Rule Filtering and Processing**: Filters and processes rules based on specific cloud platforms (AWS, Azure, GCP) and language detection.
- **JSON File Generation**: Creates separate JSON files (`rules_aws.json`, `rules_AZU.json`, `rules_gcp.json`) for each cloud platform's rules.
- **Schema Creation**: Generates a JSON schema file (`rules_schema.json`) for the rulesets.

### Second Script: Custom Ruleset Submission
- **Credential and File Checks**: Verifies the presence of Dome9 credentials and the JSON files containing the rules.
- **Load Rules from Files**: Reads the rules for AWS, Azure, and GCP from their respective JSON files.
- **API Interaction for Custom Ruleset Creation**: Submits custom rulesets to Dome9's API for each cloud platform, with a payload that includes the rules and additional metadata.

### Key Features
- **Automated Ruleset Management**: Streamlines the process of managing compliance rulesets in Dome9 for different cloud providers.
- **Custom Ruleset Creation**: Allows for the creation of tailored compliance rulesets based on specific requirements or cloud environments.
- **Versatile Script Usage**: Capable of handling multiple cloud platforms, enhancing cross-platform cloud security and compliance.

### Usage Scenario
These scripts are highly beneficial for cloud security engineers and compliance officers who utilize Dome9 for cloud security and compliance management. They simplify the process of customizing and managing compliance rulesets across multiple cloud platforms.

### Prerequisites
- Python environment with the `requests` and `pandas` libraries.
- Dome9 account with API access and valid credentials.

### Security Considerations
- Careful management of Dome9 credentials, preferably using environment variables for security.
- Ensure secure handling and storage of the generated JSON files containing the compliance rules.

---

This readme summary provides a comprehensive overview of the repository's content and its purpose, highlighting its role in facilitating Dome9 compliance ruleset management for AWS, Azure, and GCP environments. It serves as a guide for users looking to automate and streamline their cloud compliance operations using Dome9.
