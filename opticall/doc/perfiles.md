``` mermaid
sequenceDiagram
    participant User
    participant Controller
    participant AuthService
    participant ProfileValidator
    participant ProfileRepository
    participant AuditLogger

    User->>Controller: POST /api/perfiles
    Controller->>AuthService: VerifyAdminRole()
    AuthService-->>Controller: 200 OK
    Controller->>ProfileValidator: Validate(dataDTO)
    ProfileValidator-->>Controller: ValidationResult
    Controller->>ProfileRepository: CreateProfile(profileEntity)
    ProfileRepository-->>Controller: CreatedProfile
    Controller->>AuditLogger: LogCreationEvent()
    AuditLogger-->>Controller: LogSaved
    Controller-->>User: 201 Created


```
