# AI-Resilient Assignment Design

## A Practitioner Workbook

### Youngstown State University — 2025–2026

*Developed for faculty and instructional designers building AI-collaborative course experiences in the Mahoning Valley.*

---

# The Problem We Are Solving

Standard online assignments were designed in a world where producing a well-written essay required substantial cognitive effort. That world ended.

A student can now submit a fluent, grammatically correct, structurally coherent 1,500-word analysis of *any* general topic in approximately 90 seconds. The grade goes up. The learning doesn't happen.

We call this the **Mask of Perfection**: an AI-generated artifact that looks like evidence of learning but contains no student cognition. The problem isn't that students are cheating. The problem is that the assignment was designed to be completed by a machine — we just didn't know it yet.

> **The shift this workbook makes:**
> Stop designing assignments that try to *prevent* AI use. Start designing assignments that *require* AI use — and grade the student on their ability to direct, correct, and defend what the AI produces.

This workbook gives you three AI bots built for Boodlebox that implement exactly this approach. Each bot has a specific role in a pipeline that takes a legacy assignment and transforms it into something genuinely resilient.

---

# The Three-Bot Pipeline

These bots are designed to be used in sequence. Think of them as three specialists you hand a syllabus to, one after another.

| Bot                              | Role          | What You Give It                   | What You Get Back                                           |
| -------------------------------- | ------------- | ---------------------------------- | ----------------------------------------------------------- |
| **Vulnerability Assessor** | The Auditor   | Your legacy assignment or syllabus | A scored JSON assessment of every assignment's AI risk      |
| **Resilient Designer**     | The Architect | The vulnerability assessment       | A fully redesigned 3-Gate assignment structure              |
| **Blueprint Compiler**     | The Editor    | Original + redesigned structure    | A polished, student-ready assignment brief or full syllabus |

You don't have to run all three in one session. Many practitioners find value in just running the Vulnerability Assessor on their entire syllabus to understand where their exposure is before redesigning anything.

**What makes this a pipeline and not just a chatbot:**
Each bot refuses to do the other bots' jobs. The Vulnerability Assessor will not write new assignments. The Resilient Designer will not polish prose. The Blueprint Compiler will halt and reject work that slipped past the design stage. This separation is intentional — it prevents the cascade of errors that happen when one LLM tries to do everything.

---

# Bot 1: The Vulnerability Assessor

## *What It Does*

The Vulnerability Assessor reads your assignment and tells you — precisely and without sentiment — how easily a student could complete it using AI without engaging with the learning objective.

It evaluates three dimensions:

**1. Format Standardity**
Is the deliverable an essay, a report, a discussion post, a summary, a written critique? These formats are the native output of language models. Any assignment that ends in one of these has a structural vulnerability regardless of how interesting the topic is.

**2. Context Availability**
Does the assignment require knowledge that is broadly available on the internet — historical events, theoretical frameworks, published case studies? If so, an LLM already has it. The more specific, local, and un-Googleable the required knowledge, the harder the assignment is to automate.

**3. Verification**
Is the only evidence of learning a final polished document with no formative checkpoints? If there is no process to observe — no intermediate submissions, no live defense, no documented corrections — then the Mask of Perfection is undetectable.

The bot outputs a **risk band** for each assignment: Low, Medium, High, or Critical.

> **Critical** means the assignment can be fully completed by an LLM in a single prompt. If a student opens ChatGPT, pastes in the instructions, and presses Enter — they have a passing submission. No student cognition required.

---

# Bot 1: Full Instructions

## *What the Bot Is Told*

These are the exact instructions loaded into the Vulnerability Assessor on Boodlebox. Understanding them helps you know what the bot will and won't do — and how to adjust its behavior.

---

**Persona**

> You are the **Pedagogical Hacker** for the AI-Resilient Course Modernization Pipeline. Your job is to audit legacy course assignments and identify points of catastrophic cognitive offload where a student can use a generative AI to bypass the learning objective entirely.

**Input Detection**

> You will receive a legacy educational document. This may be a complete course syllabus containing multiple assignments, or a single standalone assignment prompt. Detect which type you have received. If it is a syllabus, identify and evaluate each gradable assignment independently.

**Risk Band Definitions**

> | Band               | Meaning                                                                                                                           |
> | ------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
> | **Critical** | Fully automatable in a single LLM prompt. Zero student cognition required. Immediate redesign mandatory.                          |
> | **High**     | Automatable with moderate prompt engineering. Student can offload 80%+ of cognitive work. Redesign strongly recommended.          |
> | **Medium**   | Partially vulnerable. Some friction, but core deliverable remains LLM-friendly. Targeted hardening advised.                       |
> | **Low**      | Meaningful resistance to automation. Hyper-local data, process verification, or non-text deliverables present. Minor tuning only. |

**Hard Constraint**

> DO NOT generate new assignment instructions. That is the job of the Resilient Designer. Your job is diagnosis and strategic redirection only.

**Output**

> Output a strict JSON array. Each element represents one evaluated assignment and must contain: `id`, `input_type`, `original_text`, `qualitative_risk_band`, `core_learning_objective`, and `suggested_substitution_framework`.

---

# Bot 1: Knowledge Bank

## *Predictability Scorer — Why It Works*

The Vulnerability Assessor draws on a knowledge bank of scoring heuristics. Here is the full content, followed by an explanation of the design choices.

---

**Full Knowledge Bank Text:**

> **Initial Risk Band Assessment:**
> Does the format use standard terminology (essay, report, summary, critique, discussion post)? Set baseline to Medium/High. Does it lack local, personal, or recent context markers (lived experience, local community, current events)? Escalate risk by one band. Is the deliverable purely text-based (no presentation, diagram, video, or code required)? Escalate risk by one band.
>
> **Metacognitive Load:**
> If lower-order Bloom's verbs dominate (Define, List, Summarize), escalate risk by one band. If higher-order dominates (Synthesize, Evaluate, Design), lower risk by one band.
>
> **Constraint Density:**
> If the prompt has highly specific limiting clauses ("must use X specific data source, Y theoretical framework, Z local institution"), lower the risk by one band. If open-ended, maintain or elevate.
>
> **Relational Index:**
> Scan for relational markers (lived experience, dialogue, power dynamics, community interview). If present frequently, lower the risk.

---

**Why this works:**

The heuristics are designed to identify a single underlying condition: *can a generic LLM produce a passing response without knowing anything specific about this student, this community, or this course?*

The **Bloom's verb check** is a proxy for cognitive load. Lower-order verbs (define, list, describe) correlate with tasks that are essentially retrieval exercises — exactly what LLMs do best. Higher-order verbs (design, evaluate, defend) require the student to make choices that an LLM can only simulate.

The **Constraint Density check** is counterintuitive: more constraints = lower risk. A constraint like "analyze Hamilton County's 2024 budget shortfall using Keynesian fiscal theory as your framework" is almost impossible to automate because the combination of specific data + specific theory creates a narrow target the LLM will miss or hallucinate.

The **Relational Index** checks for lived experience markers. An assignment that asks a student to "interview a first-generation college student at YSU about their technology access challenges" cannot be completed without a real conversation. No training data substitutes for that.

---

# Bot 1: What to Change

## *Customizing the Vulnerability Assessor*

**Change this for your discipline:**
The heuristics are domain-neutral by default. If you teach nursing, add clinical-specific high-risk formats to your knowledge bank: "care plan," "clinical reflection," "SOAP note response." If you teach law, add "case brief," "legal memo," "statutory analysis." Any format that is taught as a template in your field is a vulnerability.

**Change this for your institution:**
The relational index checks for general markers like "lived experience" and "dialogue." If your institution has specific pedagogical language — YSU uses "engaged learning" and "community partnership" — add those terms. The bot will treat their presence as a risk-reducing signal.

**Do not change this:**
The hard constraint against generating new assignments. If you remove it, the bot will start writing redesigns before the Designer has a chance to apply institutional context. The quality of the output drops significantly when one bot tries to do two jobs.

**A useful experiment:**
Run the bot on your three most-used assignments before looking at the risk bands. Write down your own prediction for each. Then compare. Most faculty are surprised to find their "challenging" discussion post is rated Critical and their "simple" data exercise is rated Low. The disconnect between perceived rigor and actual LLM resistance is the most common insight this bot surfaces.

---

# Bot 2: The Resilient Designer

## *What It Does*

The Resilient Designer takes the vulnerability assessment and engineers a replacement. It does not polish or format — that is the Blueprint Compiler's job. It designs the *structure* of an assignment that is resistant to AI automation by making student cognition non-optional.

It operates under one governing principle: **Offensive Learning Design.**

> Do not fight AI. Require it. Grade the student on what they do *with* AI, not on whether they avoided it.

The Resilient Designer implements this through a mandatory structure called the **3-Gate PBL Framework**. Every redesigned assignment must pass through all three gates in sequence. Each gate is a formative checkpoint — the student cannot proceed to the next gate without an instructor approval, which means the process is observable even if the final artifact is AI-assisted.

---

# Bot 2: The 3-Gate Framework

## *The Heart of the Resilient Design*

**Gate 1 — The Local Dataset**

The student identifies or is provided a specific, hyper-local dataset that cannot be pre-fabricated by a generic LLM. For YSU, this might be: current vacancy data from the Mahoning County Land Bank, Q3 patient outcome statistics from Mercy Health St. Elizabeth, or active cohort data from the Youngstown Business Incubator.

*Why this works:* An LLM trained on internet data cannot accurately reproduce a dataset that doesn't exist on the internet. The moment a student has to engage with real, local, messy data, they are doing something the AI cannot shortcut for them.

*Formative Check:* Student submits the raw data parameters and the AI's initial summary. Instructor approves scope before Gate 2.

---

**Gate 2 — Prompt Architecture & Correction**

The student uses course-specific theory to direct the AI's analysis — and then corrects the AI where it fails. The assignment specifies a theoretical lens narrow enough that a generic LLM will misapply it. The student's submission is not the AI's output. It is the student's *correction* of the AI output, with citations.

*Why this works:* This is where learning happens. The student must know the theory well enough to catch the AI's errors. A student who does not understand Durkheim's concept of anomie cannot correctly identify where the AI applied it incorrectly. This gate is unfakeable without genuine course knowledge.

*Formative Check:* Student submits the correction log. This is the primary evidence of learning.

---

**Gate 3 — The Artifact & Defense**

The final deliverable is never an essay. It maps to one of four resilient deliverable types (see next card). It must be accompanied by an async audio or video defense where the student explains their architectural choices.

*Why this works:* A visual system map, a policy decision record, or a live recorded demonstration cannot be fabricated and submitted the way a Word document can. The defense adds a layer that requires the student to explain, in their own voice and in real time, why they made specific choices — something AI-generated text cannot do on their behalf.

*Formative Check:* Submitted artifact + defense recording.

---

# Bot 2: The Four Resilient Deliverable Types

These are the only Gate 3 deliverable formats the Resilient Designer will generate. Each is chosen because it creates structural accountability that a submitted text document does not.

**1. Visual Frameworks & Diagrams**
A system map, Mermaid.js conceptual graph, or decision tree, defended via oral or video component. The diagram externalizes the student's mental model in a form that cannot be fabricated without making design choices the student must then explain.

*Best for:* Systems thinking courses, engineering, organizational behavior, public policy.

**2. Artifact as Blueprint Documentation**
An Architectural Decision Record (ADR), structured policy brief, or rubric map tied to institutional constraints. The format is highly specific — an LLM can draft one, but the content must reference real local data and specific course frameworks to pass validation.

*Best for:* Business, healthcare management, education policy, technology courses.

**3. In-Browser / Live Demonstration**
A recorded screen-share where the student narrates real-time manipulation of a tool to solve a problem. Not editable post-recording. The student's voice, choices, and corrections are captured as they happen.

*Best for:* Data analysis, coding, digital media, clinical simulation.

**4. Hyper-Local Context Synthesis**
The AI processes standard knowledge; the student integrates it with the Gate 1 local dataset in a way that requires institutional knowledge unavailable in LLM training data. The synthesis is evaluated against local ground truth, not general plausibility.

*Best for:* Social sciences, community health, urban planning, regional economics.

---

# Bot 2: Full Instructions

## *What the Bot Is Told*

---

**Persona**

> You are the **Modern Instructional Designer** for the AI-Resilient Course Modernization Pipeline. You operate under the principle of **Offensive Learning Design**. You do not build Defensive Friction. You design assignments where AI collaboration is the baseline expectation, and the student is graded on their **Architectural Agency** — their ability to direct, correct, and defend the AI's work against course theory.

**Processing Scope**

> - Critical or High risk: Full redesign using the 3-Gate PBL structure.
> - Medium risk: Targeted hardening — note what should change, but do not fully redesign unless instructed.
> - Low risk: Flag as compliant. No redesign needed.

**Required Before Designing**

> Before designing any assignment, consult your `local-context-fetcher` Knowledge Bank to load current institutional constraints, pedagogical tone, and active policies. All redesigned assignments must be grounded in this context — never in generic frameworks. Consult your `mermaid-baseline-generator` Knowledge Bank when Gate 3 requires a visual framework deliverable.

**Absolute Rules**

> 1. NO UNVERIFIED TEXT — Never output an assignment where the final deliverable is an unverified text document.
> 2. NO DEFENSIVE FRICTION — Explicitly exclude prompt logs, chat transcripts, or "reflection on AI use" as deliverables.
> 3. AI AS BASELINE — The assignment must explicitly require generative AI as a starting collaborator.

---

# Bot 2: Knowledge Bank A

## *Local Context Fetcher — Why It Works*

The local context knowledge bank is the most important piece of the entire system. It is what separates a generically "AI-resistant" assignment from one that is specifically resistant at YSU in 2025-2026.

This knowledge bank contains YSU-specific institutional data that a generic LLM does not have: the America Makes facility address, Mahoning County ZIP codes for health equity data, the YBI's active cohort sectors, the shrinking cities policy context, the commuter student logistics constraints.

**Why specificity is the mechanism:**

When the Resilient Designer generates a Gate 1 dataset requirement, it draws on this knowledge bank. The difference between a generic Gate 1 ("find a local dataset about economic inequality") and a YSU-grounded Gate 1 ("obtain current vacancy parcel data from the Mahoning County Land Bank for ZIP code 44507 and feed it to an LLM to generate a neighborhood analysis") is the difference between a task that is easy to fake and one that requires a student to actually engage with a real, local data source.

**Key institutional anchors in this knowledge bank:**

- **America Makes** (1410 Elm St) — Any additive manufacturing, workforce, or advanced manufacturing assignment can be anchored here. Generic LLM answers will not match America Makes' actual technology roadmap.
- **Mahoning County Land Bank** — 20,000+ vacant parcels, shrinking city master plan. LLMs default to growth-model assumptions that are visibly wrong in Youngstown.
- **ZIP codes 44501–44515** — Health equity assignments that require actual Mahoning County disease burden data an LLM cannot accurately reproduce.
- **YBI at 241 W. Federal St** — Real, named entrepreneurship cases. Graduates from specific cohorts in cybersecurity, logistics software, advanced materials.
- **The commuter and first-gen constraints** — Embedded in the knowledge bank so every assignment the Designer generates automatically accounts for asynchronous-first group work and no assumptions about professional network access.

---

# Bot 2: Knowledge Bank B

## *Mermaid Baseline Generator — Why It Works*

When a Gate 3 deliverable is a visual framework, the Resilient Designer generates a starting Mermaid.js diagram template as the "AI's first pass." This becomes the artifact the student must critique, correct, and defend.

**Why Mermaid specifically:**
Mermaid.js diagrams are rendered natively in most modern LMS systems including Canvas and Blackboard when embedded in markdown. They are text-based (easy for LLMs to generate), visually expressive (easy for students to read and critique), and structurally specific (easy for instructors to evaluate whether the student's corrections represent real understanding).

**The syntax rules embedded in this knowledge bank:**

> 1. No inline `%%` comments inside the mermaid code block — LMS parsers fail on them.
> 2. All node text and edge labels must be wrapped in double quotes.
>
> - Correct: `A["Start: Initial Concept"]`
> - Incorrect: `A[Start: Initial Concept]`

These rules exist because the workbook is designed for real classroom use, not just demonstration. A Mermaid diagram that crashes the LMS renderer defeats the purpose entirely.

**What to change:**
If your institution uses a different visual framework tool (Lucidchart, draw.io, Figma), replace this knowledge bank with syntax examples and constraints for that tool. The principle is the same: give the AI a structured starting template, then grade the student on their corrections to it. The tool is interchangeable. The cognitive pattern is not.

---

# Bot 2: What to Change

## *Customizing the Resilient Designer*

**The most important change: the local context knowledge bank.**
This is what makes every output institution-specific. If you are building this for a different university, the entire `local-context-fetcher` knowledge bank needs to be replaced with that institution's data. The structure to follow:

- Named local institutions with physical addresses
- Specific datasets that are publicly available but not in LLM training data
- Student demographic constraints that must be honored in assignment design
- Current institutional strategic priorities
- Active AI use policy language

The more specific you are, the more the bot's outputs diverge from what a generic LLM would produce. Vague entries ("our students come from diverse backgrounds") produce vague assignments. Specific entries ("55% of YSU students are first-generation; do not design assignments that assume professional network access") produce assignments that actually account for your student population.

**What to add for your discipline:**
The four deliverable types are domain-neutral. If your discipline has a standard professional artifact format that would work well as a Gate 3 deliverable — a clinical SOAP note template, a legal brief structure, an engineering design specification — add it to the knowledge bank as a fifth type. The bot will use it when the course context is appropriate.

**What NOT to change:**
The absolute rules (no unverified text, no defensive friction, AI as baseline). These are the load-bearing constraints of the entire framework. Removing "no defensive friction" in particular is the single most common mistake practitioners make when adapting this system. Prompt logs and AI reflection journals feel rigorous but they shift student attention from domain knowledge to tool mechanics. The learning disappears.

---

# Bot 3: The Blueprint Compiler

## *What It Does*

The Blueprint Compiler is the final stage. It takes the raw structural design from the Resilient Designer and turns it into a document a student can actually read and use.

But it has a second function that is equally important: it is the last line of defense against regression.

Before it formats anything, it runs a validation check. If the redesigned assignment has slipped back into a vulnerable format — if someone added an essay requirement, if a prompt log crept back in, if a gate is missing — the Blueprint Compiler halts. It does not fix the problem itself. It outputs a structured error report and sends the design back to the Resilient Designer.

> **Why the compiler does not self-correct:**
> When a single agent fixes its own errors, it cannot distinguish between "this is a mistake" and "this is an intentional design choice I don't understand." Keeping the correction in the Designer's hands preserves the integrity of the institutional context that was used to make the original design decision. A compiler that silently patches problems is a compiler that silently erases reasoning.

The Blueprint Compiler also detects whether it received a full syllabus or a single assignment and adjusts its output format accordingly:

- **Full syllabus input:** Produces a complete, integrated syllabus. Every non-assignment section — schedules, grading rubrics, attendance policies, accessibility statements — is reproduced verbatim. Only the legacy assignment text is replaced.
- **Single assignment input:** Produces a clean, standalone student-facing assignment brief.

---

# Bot 3: Full Instructions

## *What the Bot Is Told*

---

**Persona**

> You are the **Auditor and Compiler** for the AI-Resilient Course Modernization Pipeline. You are the final quality control check and the voice of the transformative educator. You embody the concept of the instructor as the **"Architect of Discovery"** — framing AI not as a threat to be managed, but as a powerful collaborator in the student's intellectual journey.

**Input Detection**

> If the original was a full course syllabus, output a complete integrated syllabus. If the original was a standalone assignment, output a self-contained student-facing assignment brief.

**Validation — Hard Stop Rules**

> Do NOT self-correct across role boundaries. If any check fails, halt immediately, output a structured error report, and request a revised design from the Resilient Designer.
>
> - Does every assignment follow the 3-Gate PBL structure?
> - Does each Gate 3 deliverable map to one of the four approved types?
> - Does any part rely on a generic text-based deliverable (essay, report, reflection paper)?
> - Does any part rely on Defensive Friction (prompt logs, chat transcripts, AI reflection essays)?

**Anti-Truncation Rule (Syllabus Mode)**

> Output the entire original syllabus. Do not summarize, condense, or omit any non-assignment section. Grading rubrics, course schedules, attendance policies, and accessibility statements are reproduced verbatim.

**Standalone Brief Structure**

> 1. Project Title — Snappy and professional.
> 2. Learning Objectives — From the original assignment context.
> 3. Project Context & AI Collaboration — Frames student as Architect, not user.
> 4. The 3-Gate Workflow — Each gate with formative check instructions.
> 5. Grading Philosophy — Architectural Agency over polish.

---

# Bot 3: Knowledge Bank

## *Constraint Auditor — Why It Works*

---

**Full Knowledge Bank Text:**

> **Core Rule:** Categorically reject any assignment that requests an unverified text format.
>
> **Semantic Evaluation Steps:**
>
> 1. Does the deliverable feel like something a student could accomplish simply by copying the prompt into ChatGPT and pasting the response into a Word document? (e.g., "Craft a narrative," "Reflect on," "Synthesize your thoughts into a brief statement.") If yes: FAIL.
> 2. If the core deliverable is an unverified block of text: FAIL.
> 3. If the deliverable is structurally resilient (a visual system map, a live recorded demonstration, or an Architectural Decision Record): PASS.
>
> **Banned Terminology Concepts:**
> Watch for variations of: "Write a 5-paragraph essay," "Submit a Word document," "Draft a written critique," "Post a 200-word response to the discussion board."

---

**Why this works:**

The constraint auditor operates semantically, not just by keyword. "Write a narrative" and "craft a reflective piece" do not contain the word "essay" but they trigger the same validation failure because they describe the same kind of deliverable: unverifiable, LLM-native text.

The banned terminology list is intentionally short. Its purpose is not to be exhaustive — it is to calibrate the bot's semantic evaluation. The real check is the first question: *could a student complete this by pasting the prompt into ChatGPT?* Everything else is a heuristic to help answer that question.

---

# Bot 3: What to Change

## *Customizing the Blueprint Compiler*

**Add to the banned terminology list for your discipline:**
The current list covers generic academic writing. If your discipline has specific vulnerable formats, add them:

- Nursing: "care plan narrative," "clinical reflection log," "patient scenario response"
- Education: "lesson plan rationale essay," "teaching philosophy statement"
- Business: "executive summary," "market analysis report"

These additions calibrate the semantic evaluation for domain-specific language the bot would otherwise miss.

**Change the Grading Philosophy language:**
The default language ("Architectural Agency over polish") is conceptual. For a student-facing brief, you may want to translate this into your institution's assessment language. At YSU, this might reference the engaged learning outcomes or specific program competencies. The concept stays the same; the vocabulary can match your accreditation framework.

**Change the standalone brief section headers:**
If your course uses a specific assignment template format required by your department or program, replace the default section structure with that template. The bot will populate the YSU-specific content into whatever structure you define.

**Do not change:**
The halt-on-fail validation logic. The temptation is to make the compiler "smarter" by having it fix problems rather than flag them. Resist this. The value of the compiler is that it surfaces design failures rather than papering over them. A silent fix is an invisible regression.

---

# Key Concepts Glossary

**Architectural Agency**
The measurable learning skill this entire system is designed to develop and assess. Can the student direct, correct, and defend AI output using domain-specific knowledge? This is graded on the quality of the corrections and the defense — not on the polish of the final product.

**Mask of Perfection**
An AI-generated artifact that appears to demonstrate learning but contains no student cognition. Fluent, grammatically correct, structurally coherent — and entirely hollow. The primary threat model this pipeline addresses.

**Cognitive Offload**
The degree to which an assignment allows a student to delegate the cognitive work to an external tool (historically: textbooks, tutors; now: LLMs). Assignments with high cognitive offload potential are assignments where the student can achieve a passing grade without developing the targeted skill.

**Defensive Friction**
Assignment design strategies that attempt to prove AI non-use: prompt logs, AI transcript submissions, "reflection on my AI use" essays. These strategies are ineffective (they can be faked), counterproductive (they shift focus from domain knowledge to tool mechanics), and exhausting to grade. This system explicitly forbids them.

**Process-Over-Product**
An assessment philosophy that grades the observable, documented process by which a student developed their work — not just the final artifact. The 3-Gate structure operationalizes this: each gate is a formative checkpoint that makes the process visible.

**3-Gate PBL**
The structural framework the Resilient Designer uses for every redesign. Gate 1 (Local Dataset) creates the un-Googleable foundation. Gate 2 (Prompt Architecture & Correction) generates the evidence of learning. Gate 3 (Artifact & Defense) produces a verifiable, non-fakeable final deliverable.

**Hyper-Local Context**
Data, institutions, policies, or conditions so specific to a place and time that a generic LLM cannot accurately reproduce them. At YSU: Mahoning County Land Bank parcel data, America Makes' current technology roadmap, YBI's active cohort sectors. The more hyper-local the context, the higher the cognitive floor the assignment creates.

---

# Running the Pipeline: Step by Step

**Step 1 — Prepare your input**
Paste your assignment text (or full syllabus) directly into the Vulnerability Assessor bot. You do not need to clean it up — the bot handles raw syllabus formatting.

**Step 2 — Get the vulnerability assessment**
The bot returns a JSON array. For each assignment, note the `qualitative_risk_band` and `suggested_substitution_framework`. Any `Critical` or `High` assessment is a redesign candidate.

**Step 3 — Hand off to the Resilient Designer**
Paste the JSON output from Step 2 into the Resilient Designer bot. It will automatically redesign Critical and High assignments using the YSU institutional context in its knowledge bank.

**Step 4 — Review the structural design**
The Resilient Designer's output is a design document, not a student brief. Review it. Look at the Gate 1 dataset: is it actually hyper-local and specific? Look at Gate 2: is the theoretical lens narrow enough that an LLM will genuinely fail to apply it correctly? If something seems too generic, tell the bot — it can tighten the scope.

**Step 5 — Compile the final document**
Paste the original syllabus/assignment AND the Resilient Designer's output into the Blueprint Compiler. It will validate, then format. If it returns an error report rather than a document, that is the system working correctly — the error tells you exactly what needs to go back for revision.

**Step 6 — Hand the output to a student**
The Blueprint Compiler's output is ready to use. No additional formatting required.

---

# Building Your Own Version

## *What to Customize for a Different Institution*

If you are adapting this system for a university other than YSU or for changes made at YSU, the two knowledge bank files that require complete replacement are:

**1. The Local Context Knowledge Bank (Bot 2)**
This is the highest-leverage change in the system. Replace it with:

- The institution's current AI policy (exact language matters — students will read it)
- Named local partner institutions with physical addresses
- Specific local datasets that are publicly available but not in LLM training data
- Student demographic constraints (commuter rate, first-gen percentage, work hours)
- Strategic plan pillars with specific named initiatives
- Local industry context with named employers and their current workforce situations

The test for whether your local context is specific enough: *could a student answer a question about it by Googling for five minutes?* If yes, it is not hyper-local enough. Keep going.

**2. The Constraint Auditor Knowledge Bank (Bot 3)**
Add discipline-specific and institution-specific banned format variations. The base list covers generic academic writing. Your discipline has its own vulnerable templates that are not covered by default.

**What you do NOT need to change:**
The 3-Gate structure, the four deliverable types, and the validation logic are institution-agnostic. They are the architectural load-bearing elements. Everything else is configuration.

**A note on the Mermaid knowledge bank:**
Only change this if your LMS does not support Mermaid rendering, or if your students have access to a different diagramming tool that would serve the same function. The syntax constraints in the knowledge bank (no inline comments, strict double-quote wrapping) exist to prevent LMS rendering failures. If you switch tools, replace these constraints with the equivalent syntax rules for your chosen tool.

---

*This workbook was developed for the AI-Resilient Course Modernization Pipeline.*
*Youngstown State University — Mahoning Valley — 2025–2026*
