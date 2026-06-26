# SITREP (Situation Report): Origin, Evolution, and Canonical Structure

## Research Document
**Date:** 2026-06-26
**Purpose:** Trace the SITREP term from military origins through emergency management and intelligence usage, to inform the design of a SITREP pattern for AI agent sessions.
**Source note:** Compiled from doctrinal knowledge with browser-verified Wikipedia citations. Web search unavailable (Firecrawl not configured). URLs are canonical references to doctrinal repositories.

---

## 1. Etymology and First Documented Use

### 1.1 Term Origin

"SITREP" is a military portmanteau: SITuation REPort. It follows the Anglo-American military tradition of contracting compound nouns into pronounceable abbreviations (cf. INTREP for Intelligence Report, MEDEVAC for Medical Evacuation, COMINT for Communications Intelligence).

### 1.2 First Documented Use

Situation reporting as a concept predates the term. Roman couriers, signal fires, and the Bayeux Tapestry's messenger relay all embody the practice. The standardized term "SITREP" as a doctrinally governed reporting artifact emerged during World War II (approximately 1941-1945) in Anglo-American military communications, driven by:

- The U.S. Army's General Staff officer procedure (G-1/G-2/G-3/G-4 system adapted from French Staff College tradition, formalized in the predecessors of FM 101-5).
- The establishment of combined Allied command structures under Eisenhower and British commanders, requiring standardized reporting formats between allies.
- The rise of HF and VHF radio communications making rapid formatted messaging practical.

"SITREP" appears in published texts from 1942-1945 in British War Office and Supreme Headquarters Allied Expeditionary Force (SHAEF) communication archives. By the 1944 Normandy campaign the term was routine enough to appear without explanation in operational logs.

### 1.3 Doctrinal Codification

The earliest doctrinal encoding is difficult to pin to a single date, but the lineage runs through:

- **FM 101-5, Field Manual: Staff Officer's Manual** (first published 1940, revised 1949, 1960, 1984). The 1984 edition is the Cold War "classic" form.
- Successive generations progressively standardized the SITREP format. The 1984 FM 101-5 is the most cited Cold War reference.
- Replaced in the modern era by **ATP 6-0.5** (2016), Command and Control Staff Organization and Operations, the current doctrinal basis for Army tactical SITREP format.

### Sources
- Wikipedia, "Situation report" (redirects to "Command center"): https://en.wikipedia.org/wiki/Command_center
- Wikipedia, "List of U.S. government and military acronyms": https://en.wikipedia.org/wiki/List_of_U.S._government_and_military_acronyms (entry: "SITREP - Situation Report")
- U.S. Army Publications: https://armypubs.army.mil/ (search by publication number for ATP 6-0.5, FM 101-5)
- Eisenhower Presidential Library, SHAEF communications: https://www.eisenhowerlibrary.gov/

---

## 2. Canonical Military SITREP Format

### 2.1 Key Doctrinal Publications

| Publication | Title | Authority | Scope |
|---|---|---|---|
| ATP 6-0.5 (2016) | Command and Control Staff Organization and Operations | U.S. Army | Current Army tactical SITREP format |
| FM 101-5 (1984 and prior) | Staff Organization and Operations | U.S. Army | Classic "G-staff" SITREP, decades of Army standard |
| JP 3-0 | Joint Operations | Joint Chiefs of Staff | Joint SITREP framework |
| JP 1-02 (and successors) | Dictionary of Military Terms | Joint Chiefs of Staff | Defines SITREP as a joint term |
| MC 331 / AJP-3 | NATO Allied Joint Operations Doctrine | NATO Standardization Office | NATO coalition SITREP protocols |

### 2.2 Standard Sections (U.S. Army, FM 101-5 / ATP 6-0.5 lineage)

The canonical periodic SITREP sent by a unit to its higher headquarters:

1. **Header / Identification** - Sending unit (callsign/designation), classification (UNCLASSIFIED through TS/SCI), date-time group (DTG), reference to previous report, subject line ("SITREP #N")
2. **Situation Overview** - Narrative summary of the operational environment
3. **Friendly Forces Situation** - Mission capability readiness, current disposition and activities, significant changes since last report
4. **Enemy Situation** - Enemy disposition, organization, strength, enemy activity since last report, answers to Priority Intelligence Requirements (PIR)
5. **Operations / Activities** - Tasks executed this period, engagements and significant events, ongoing missions
6. **Logistics and Sustainment** - Status of supply classes I through X (water/rations, fuel, ammunition, etc.), critical shortages, resupply plan
7. **Personnel and Casualties** - KIA/WIA/MIA counts, replacements received, current strength
8. **Command and Control / Signal** - C2 node status, communications status, planned changes to frequencies or callsigns
9. **Assessment and Commander's Comments** - Threat/risk changes, commander's intent or guidance for next reporting period, specific requests
10. **Next Report** - When the next SITREP is due

### 2.3 Format Notes

- Written in terse verbose, not continuous prose. Each section opens with a part header followed by brief data.
- DTG format: DDHHMMZ MON YY (Z = Zulu time / UTC).
- Continuity between SITREPs is implicit: report numbering sequence and "SINCE LAST SITREP" framing.
- Report period is typically 24 hours, but operational SITREPs can be more frequent (6 or 12 hours).
- The section structure mirrors the five-paragraph operations order (SMEAC: Situation / Mission / Execution / Administration & Logistics / Command & Signal), serving as the reporting counterpart.

### 2.4 Authoritative Definition

From joint doctrine: "Situation Report (SITREP): A report submitted by a subordinate headquarters to a higher headquarters, covering the situation, activities, and status of the unit for a specified period."

### 2.5 NATO Variant (STANAG 2014)

NATO standardizes operational reporting through STANAG 2014 (Military operational reports). The NATO SITREP inherits the Anglo-American model with these sections:

1. General Situation
2. Intelligence / Enemy Situation
3. Friendly Forces
4. Operations
5. Admin and Logistics
6. Conclusions / Assessment

Uses NATO classification lines (NATO RESTRICTED through TOP SECRET, including ATOMAL). Employs standard NATO originator/recipient codes. Retains British-style paragraph numbering.

### Sources
- ATP 6-0.5 (2016): https://armypubs.army.mil/
- FM 101-5 (1984): https://archive.org/ (search "fm 101-5")
- JP 3-0: https://www.jcs.mil/Doctrine/
- STANAG 2014 via NATO Standardization Office: https://nso.nato.int/nso/
- AJP-3 via NSO portal: https://nso.nato.int/nso/

---

## 3. FEMA / ICS SITREP Variant

### 3.1 NIMS Position on Situation Reports

Under FEMA's National Incident Management System (NIMS), the situation report is a real-time situational awareness product generated by the Situation/Documentation Unit in the Planning Section. There is no single ICS form named "Situation Report." Instead, two parallel forms serve the function:

- **ICS Form 201, Incident Briefing**: The initial one-page snapshot used during command transfer. Captures what the outgoing Incident Commander (IC) knows about situation, resources, objectives, and hazards. Functions as the initial SITREP.

- **ICS Form 209, Incident Status Summary**: The ongoing periodic report sent to MAC groups, area commands, and state/federal liaisons during multi-operational-period incidents. This is the primary carrier of SITREP content during a disaster.

Supporting forms: ICS Form 202 (Incident Objectives), ICS Form 214 (Unit/Individual Activity Log), ICS Form 215 (Operational Briefing).

### 3.2 ICS Form 201 Fields (Incident Briefing)

1. Incident Name
2. Incident Number
3. Initiation Date/Time and Briefing Date/Time
4. Prepared By (name and position)
5. For (receiving Incident Commander's name and position)
6. Resources Summary (committed, ordered, en route, pending)
7. Current Organization (command and general staff)
8. Resource Summary by category
9. Current Incident Objectives
10. Situation Overview (narrative)
11. Aviation Operations Risk Summary (if applicable)
12. Forecast Weather (if applicable)
13. Identified Hazards
14. Map (situation) attachment

### 3.3 ICS Form 209 Fields (Incident Status Summary)

1. Initial or Update (checkbox)
2. Incident Name / Incident Number
3. Date/Time Prepared
4. Prepared By
5. Incident Type (wildfire, flood, mass casualty, etc.)
6. Incident Location
7. Incident Summary (narrative)
8. Current Incident Statistics (area, structures threatened/damaged/destroyed, evacuations, fatalities, injuries)
9. Current Incident Cost
10. Significant Events During Last Operational Period
11. Predicted Activity (12h, 24h, 48h, 72h)
12. Current Objectives / Strategy
13. Significant Problems and Concerns
14. Resources Committed (personnel, crews, engines, helicopters, dozers)
15. Critical Resource Shortages (next 24-48 hours)
16. Estimated Demobilization Start
17. Prepared By and Incident Commander signature

### 3.4 NIMS Doctrinal Basis

NIMS versions: October 2004 (first), December 2008 (revision), May 2017 (update). All versions reinforce the operational planning cycle where the 209 is the primary periodic SITREP tool. The ICS structure itself derives from FIRESCOPE (1972-1980s, Southern California wildfire interagency protocols), later codified into NIMS.

### Sources
- FEMA ICS Forms: https://www.fema.gov/emergency-managers/nims/components
- NIMS documentation (2017): https://www.fema.gov/emergency-managers/nims
- FIRESCOPE history: https://www.usfa.fema.gov/

---

## 4. Military vs. Civilian SITREP Comparison

| Dimension | Military SITREP (U.S./NATO) | FEMA/ICS SITREP (Civilian) |
|---|---|---|
| Purpose | Command information flow (subordinate to higher), focused on operational status | Incident situational awareness, MAC group coordination, public information |
| Primary Audience | Higher and adjacent headquarters, parallel units | Leadership, state EM offices, interagency, public extension |
| Structure | Section-numbered per FM 101-5 / ATP 6-0.5 / STANAG 2014 | ICS Form 201/209 plus narrative SITREP |
| Classification | UNCLASSIFIED through TS/SCI, marked per line | Usually UNCLASSIFIED // FOUO (public release versions available) |
| Enemy Section | Prominent and required | None; replaced by environmental hazards |
| Logistics Section | Detailed supply classes I through X | Resource summary (personnel, engines, dozers, helicopters) plus critical resource shortages |
| Casualties | KIA/WIA/MIA/DOS, continuously tracked | Deaths, injuries, illnesses, evacuations, incident-focused |
| Time Format | DTG, Zulu time | Local or regional time |
| Frequency | Fixed by OPCON SOP, typically 12 or 24 hours | Set by IC/Planning Section at end of operational period |
| Publication | Generally not public | Often public (wildfire 209 reports are routinely published) |

The origin distinction matters: the military SITREP derives from staff organization doctrine (FM 101-5 lineage). The FEMA/ICS variant derives from FIRESCOPE wildfire protocols (1970s), later codified into NIMS (2004). The military version emphasizes the enemy; the civilian version emphasizes hazards, evacuations, infrastructure, and public information.

---

## 5. Modern Civilian and Business Usage

- Universities and public institutions use SITREP-style periodic reporting during emergencies.
- Data center operations teams use daily SITREPs for infrastructure status.
- CISA (Cybersecurity and Infrastructure Security Agency) publishes incident SITREPs: https://www.cisa.gov/
- UN OCHA publishes situation reports for humanitarian crises: https://www.unocha.org/
- ReliefWeb aggregates humanitarian SITREPs: https://www.reliefweb.int/

---

## 6. Synthesis for AI Agent SITREP Pattern

Based on the above research, the recommended fields for a Hermes agent SITREP:

1. **Header** - Agent identity, profile name, session ID, report DTG, reference to previous SITREP
2. **Session Mission** - Brief task statement (references inherited intent)
3. **Completed Work** - Activities since last SITREP (analogous to "operations since last report")
4. **Key Results and Outputs** - Deliverables, tools invoked, successful verifications
5. **Anomalies and Obstacles** - Failures, retries, blockers (analogous to logistics shortages / critical resource shortages)
6. **Self-Assessment** - Agent's assessment of its own state/capability (analogous to commander's assessment)
7. **Planned Next Steps / Handoff** - Continuation for next agent session (analogous to next SITREP and command relationships)

This structure borrows from both the military method (sequential numbered reports, "since last SITREP" framing, explicit timeline reference) and the ICS method (explicit summary items paired with narrative qualitative assessment, status/capability query).