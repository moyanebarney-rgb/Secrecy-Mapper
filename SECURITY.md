Security Policy

1. Purpose

Secrecy Mapper is an evidence-driven analytical system designed to transform structured records into traceable entity-relationship networks.

Security, data integrity, source provenance and analytical reproducibility are core project requirements.

2. Data Handling

The following principles apply:

- Synthetic data must be used during initial development and testing.
- Real-world datasets must not be introduced without an explicit data-handling assessment.
- Personal information must not be collected unnecessarily.
- Sensitive, confidential or unlawfully obtained information must not be committed to this repository.
- Raw source records must remain distinguishable from processed analytical outputs.
- Evidence references must be preserved throughout the analytical pipeline.

3. Credentials and Secrets

Never commit:

- API keys
- Passwords
- Authentication tokens
- Private keys
- Database credentials
- Private certificates

Environment-specific credentials must be stored outside version control.

The ".env.example" file may contain safe configuration defaults and placeholders only.

4. Evidence Integrity

Analytical outputs must preserve:

- Source references
- Entity identifiers
- Relationship identifiers
- Confidence assessments
- Processing and validation records

Changes to source data or analytical transformations should be traceable.

Generated outputs must not be represented as original source evidence.

5. Analytical Integrity

Network position, centrality, connectivity and other structural metrics must not independently be interpreted as evidence of criminal conduct, misconduct or wrongdoing.

Analytical findings must distinguish:

- Verified source information
- Entity-resolution assumptions
- Inferred relationships
- Confidence assessments
- Unresolved uncertainty

6. Vulnerability Reporting

If you identify a security vulnerability, report it privately to the repository maintainer.

Do not publicly disclose exploitable vulnerabilities before they have been assessed.

Include:

- A description of the vulnerability
- Steps to reproduce it
- Potential impact
- Relevant technical evidence

7. Development Security

The project should maintain:

- Dependency management and review
- Automated testing
- Input validation
- Secure handling of local configuration
- Reproducible analytical outputs
- Appropriate separation between raw data and generated evidence

8. Scope

This policy applies to the Secrecy Mapper repository, its source code, configuration, test datasets and generated analytical artefacts.

The policy will evolve as the project moves from its initial synthetic-data implementation toward more advanced analytical capabilities.
