# Requirements Document

## Introduction

The Health Risk Assessment System enables users to assess health risks through WhatsApp messages or phone calls. An AI evaluates symptoms and classifies risk levels into three categories: home care (low risk), PHC visit (moderate risk), or emergency (high risk). ASHA workers can track patients and prioritize cases based on risk classifications.

## Glossary

- **System**: The Health Risk Assessment System
- **User**: A person seeking health risk assessment
- **ASHA_Worker**: Accredited Social Health Activist who tracks and manages patient cases
- **Risk_Level**: Classification of health risk (Home_Care, PHC_Visit, or Emergency)
- **Assessment**: The process of evaluating symptoms and determining risk level
- **Symptom_Data**: Information about user's health symptoms collected via WhatsApp or phone
- **Case**: A patient record containing assessment results and tracking information
- **WhatsApp_Channel**: Communication channel for text-based symptom reporting
- **Phone_Channel**: Communication channel for voice-based symptom reporting

## Requirements

### Requirement 1: Symptom Collection via WhatsApp

**User Story:** As a user, I want to report my symptoms via WhatsApp messages, so that I can get a health risk assessment without making a phone call.

#### Acceptance Criteria

1. WHEN a user sends a WhatsApp message to the System, THE System SHALL receive and store the message content
2. WHEN the System receives a WhatsApp message, THE System SHALL extract symptom information from the message text
3. WHEN symptom extraction is complete, THE System SHALL acknowledge receipt to the user within 30 seconds
4. IF the message content is unclear or incomplete, THEN THE System SHALL request clarification from the user
5. THE System SHALL support multiple messages from the same user to build a complete symptom profile

### Requirement 2: Symptom Collection via Phone Call

**User Story:** As a user, I want to report my symptoms via phone call, so that I can provide detailed information through conversation.

#### Acceptance Criteria

1. WHEN a user calls the System phone number, THE System SHALL answer and initiate symptom collection
2. WHILE the call is active, THE System SHALL use voice recognition to capture symptom information
3. WHEN voice recognition fails to understand input, THE System SHALL ask the user to repeat or clarify
4. WHEN the call ends, THE System SHALL have captured all necessary symptom data for assessment
5. THE System SHALL convert voice data to structured symptom information within 60 seconds of call completion

### Requirement 3: AI Risk Assessment

**User Story:** As a user, I want the AI to evaluate my symptoms and determine my risk level, so that I know what action to take.

#### Acceptance Criteria

1. WHEN complete Symptom_Data is available, THE System SHALL perform an Assessment within 2 minutes
2. THE System SHALL classify each Assessment into exactly one Risk_Level: Home_Care, PHC_Visit, or Emergency
3. WHEN the Risk_Level is Home_Care, THE System SHALL provide home care recommendations
4. WHEN the Risk_Level is PHC_Visit, THE System SHALL provide PHC location information and recommended timeframe
5. WHEN the Risk_Level is Emergency, THE System SHALL provide emergency contact information and urgent action guidance
6. THE System SHALL base risk classification on medically validated symptom patterns and severity indicators

### Requirement 4: Assessment Result Delivery

**User Story:** As a user, I want to receive my risk assessment results through the same channel I used for reporting, so that I can understand my health status and next steps.

#### Acceptance Criteria

1. WHEN an Assessment is complete, THE System SHALL deliver results to the user within 30 seconds
2. WHERE the user contacted via WhatsApp_Channel, THE System SHALL send results via WhatsApp message
3. WHERE the user contacted via Phone_Channel, THE System SHALL deliver results via SMS or callback
4. THE System SHALL include the Risk_Level, recommended actions, and relevant contact information in all result messages
5. THE System SHALL use clear, non-technical language appropriate for general users

### Requirement 5: Case Creation and Storage

**User Story:** As an ASHA worker, I want each assessment to create a case record, so that I can track patients over time.

#### Acceptance Criteria

1. WHEN an Assessment is completed, THE System SHALL create a Case record
2. THE Case SHALL contain user contact information, Symptom_Data, Risk_Level, assessment timestamp, and recommended actions
3. THE System SHALL assign a unique identifier to each Case
4. THE System SHALL store Cases securely with appropriate data protection
5. WHEN a user submits multiple assessments, THE System SHALL link Cases to the same user profile

### Requirement 6: ASHA Worker Case Dashboard

**User Story:** As an ASHA worker, I want to view all cases in a dashboard, so that I can monitor patient health in my area.

#### Acceptance Criteria

1. WHEN an ASHA_Worker logs into the System, THE System SHALL display a dashboard of all Cases
2. THE System SHALL organize Cases by Risk_Level with Emergency cases displayed most prominently
3. THE System SHALL show case details including user contact, symptoms, risk level, and assessment time
4. THE System SHALL allow filtering Cases by Risk_Level, date range, and follow-up status
5. THE System SHALL update the dashboard in real-time when new Cases are created

### Requirement 7: Case Prioritization

**User Story:** As an ASHA worker, I want cases automatically prioritized by risk level, so that I can focus on the most urgent patients first.

#### Acceptance Criteria

1. THE System SHALL rank Cases with Emergency Risk_Level as highest priority
2. THE System SHALL rank Cases with PHC_Visit Risk_Level as medium priority
3. THE System SHALL rank Cases with Home_Care Risk_Level as lowest priority
4. WHEN multiple Cases have the same Risk_Level, THE System SHALL prioritize by assessment timestamp (most recent first)
5. THE System SHALL display priority ranking visually in the dashboard

### Requirement 8: ASHA Worker Case Actions

**User Story:** As an ASHA worker, I want to mark cases with follow-up actions, so that I can track my interventions and patient progress.

#### Acceptance Criteria

1. WHEN an ASHA_Worker views a Case, THE System SHALL provide options to add follow-up notes
2. THE System SHALL allow ASHA_Worker to mark a Case as contacted, in-progress, or resolved
3. WHEN a Case status is updated, THE System SHALL record the timestamp and ASHA_Worker identifier
4. THE System SHALL allow ASHA_Worker to schedule follow-up reminders for specific Cases
5. WHEN a follow-up reminder is due, THE System SHALL notify the assigned ASHA_Worker

### Requirement 9: User Privacy and Data Security

**User Story:** As a user, I want my health information kept private and secure, so that my sensitive data is protected.

#### Acceptance Criteria

1. THE System SHALL encrypt all Symptom_Data and Case information at rest and in transit
2. THE System SHALL require authentication for ASHA_Worker access to the dashboard
3. THE System SHALL log all access to Case records with user identifier and timestamp
4. THE System SHALL comply with applicable health data privacy regulations
5. WHEN a user requests data deletion, THE System SHALL remove all associated Cases and Symptom_Data within 30 days

### Requirement 10: System Availability and Reliability

**User Story:** As a user, I want the system to be available when I need it, so that I can get timely health assessments during emergencies.

#### Acceptance Criteria

1. THE System SHALL maintain 99.5% uptime during operational hours
2. WHEN the System experiences downtime, THE System SHALL provide an automated message indicating expected restoration time
3. THE System SHALL process WhatsApp messages and phone calls concurrently without performance degradation
4. THE System SHALL handle at least 100 concurrent assessments without service interruption
5. WHEN system load exceeds capacity, THE System SHALL queue requests and process them in order received
