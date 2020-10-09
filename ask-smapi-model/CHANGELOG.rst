=========
CHANGELOG
=========

1.0.0
-----

* Initial release of ask smapi models.

1.1.0
~~~~~

This release contains the following changes : 

- Add model definitions for new `APIS related to slot type management <https://developer.amazon.com/en-US/docs/alexa/smapi/create-a-slot-type-to-use-in-multiple-skills.html>`__. Skill developers can create slot types outside the context of a skill and use it across multiple skills.



1.1.1
^^^^^

This release contains the following changes : 

- Updated properties for `skill response <https://developer.amazon.com/en-US/docs/alexa/smapi/skill-operations.html#response-4>`__ in `ListSkills` API.
- Updated interaction model values for `validation rules <https://developer.amazon.com/en-US/docs/alexa/custom-skills/validate-slot-values.html#validation-rules>`__.


1.2.0
~~~~~

This release contains the following changes : 

- APIs and model definitions for new `Audit Logs API <https://developer.amazon.com/en-US/docs/alexa/smapi/audit-logs-api.html>`__. Skill developers can use the Audit Logs API to get logs that show history of calls made to the Skill Management API(SMAPI). The logs include information about each operation including the timestamp, response code, and source.
- APIs and model definitions for new `Skill Simulations V2 API <https://developer.amazon.com/en-US/docs/alexa/smapi/skill-simulation-api.html>`__. The Skill Simulation API enables skill developers to simulate skill execution. You can test your skill and see the intent that a simulated device returns from your interaction model.


1.3.0
~~~~~

This release contains the following changes : 

- APIs and model definitions for new `Catalog V0 API <https://developer.amazon.com/en-US/docs/alexa/smapi/catalog-content-upload.html>`__. You can improve the customer experience for your skill by using the Catalog Content Upload APIs to upload your content catalog so that Alexa can access it. This allows the Alexa voice model to dynamically resolve customer utterances by referencing the catalog data as part of your Alexa skill.

- APIs and model definitions for new `SLENS V0 API <https://developer.amazon.com/en-US/docs/alexa/sdns/skill-development-notifications-api.html>`__. Alexa Skill Development Notifications Service (SDNS) enables you to receive notifications about Alexa skill development events that you trigger using the Alexa Skill Management API (SMAPI) or the Alexa Skills Kit Command-Line Interface (ASK CLI).

- Model definitions for new `Skill Event Schema <https://developer.amazon.com/en-US/docs/alexa/sdns/skill-development-event-schemas.html>`__. It describes the schemas for the events, which include skill manifest updates, certification updates, publish-to-live updates, and interaction model updates.

- Updated Interaction Model values with `Skill Model Sensitivity tuning <https://developer.amazon.com/en-US/docs/alexa/custom-skills/standard-built-in-intents.html#adjust-sensitivity>`__.


1.3.1
^^^^^

- Updated `SkillManifestPrivacyAndCompliance <https://developer.amazon.com/en-US/docs/alexa/smapi/skill-manifest.html#privacyandcompliance>`__ and `SkillManifestEndpoint <https://developer.amazon.com/en-US/docs/alexa/smapi/skill-manifest.html#endpoint>`__ schema definitions.
- Updated description field on catalog APIs and in Skill package APIs.
- Updated create skill and get skill status APIs for Alexa Hosted Skills
- Changed argument parameters of few models definitions from optional to required.


1.3.2
^^^^^

This release contains the following changes : 

- Fixes the interaction model status structure in `GetSkillStatus` API.


1.4.0
~~~~~

This release contains the following changes : 

- Added support for `NLU Evaluation APIs <https://developer.amazon.com/en-US/docs/alexa/smapi/nlu-evaluation-tool-api.html>`__.


1.5.0
~~~~~

This commit contains the following changes : 

- `Conflict Detection API <https://developer.amazon.com/en-US/docs/alexa/smapi/utterance-conflict-detection-api.html>`__ support.
- `Get skill credentials API <https://developer.amazon.com/en-US/docs/alexa/smapi/skill-credentials-api.html>`__ support.
- `NLU Evaluation and Annotation Sets API <https://developer.amazon.com/en-US/docs/alexa/smapi/nlu-evaluation-tool-api.html>`__ support.
- Enum fix for hosted skills.


1.5.1
^^^^^

This release contains the following changes : 

- Removed invalid objects from the models.


1.6.0
~~~~~

This release contains the following changes : 

- New models for `ASR evaluations API <https://developer.amazon.com/en-US/docs/alexa/asr/about-asr.html>`__
- minor bug fixes in existing models.


1.7.0
~~~~~

This release contains the following changes : 

- general bug fixes and updates


1.7.1
^^^^^

This release contains the following changes : 

- general bug fixes and updates


1.7.2
^^^^^

This release contains the following changes :

- Added new metadata, removed requirements and updated descriptions for enabling save incomplete ASR annotation sets.


1.7.3
^^^^^

This release contains the following changes :

- minor bug fixes in existing models.


1.8.0
~~~~~

This release contains the following changes : 

- New models for `Jobs Definitions API <https://developer.amazon.com/en-US/docs/alexa/smapi/manage-update-jobs.html>`__


1.8.1
^^^^^

This release contains the following changes : 

- Fix the model definition of `AccountLinkingRequest body <https://developer.amazon.com/en-US/docs/alexa/smapi/account-linking-schemas.html#accountlinkingrequest-object>`__.


1.8.2
^^^^^

This release contains the following changes : 

- Updating model definitions
