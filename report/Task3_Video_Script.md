# Task 3 Video Script – Apache NiFi Demo
**Presenter:** Sukhjeet Singh Sekhon
**Task:** Task 3 – Apache NiFi Dataflow Automation
**Target length:** ~3–4 minutes

---

## [INTRO — Look at the camera]

> "Hi, my name is Sukhjeet Singh Sekhon and I'm presenting Task 3 of our Data Engineering coursework.
> In this video I'll be demonstrating an automated Apache NiFi data pipeline that pulls book data
> from our MySQL database and saves it as a JSON file — completely automatically, no manual scripts needed."

---

## [Switch to screen — NiFi canvas, top level view]

> "So here I am in the Apache NiFi UI running locally.
> You can see I've created a Process Group called **DataEngineering** — exactly as specified in the brief.
> Let me open it up."

*(Double-click into the DataEngineering process group)*

---

## [Inside the group — show all 3 processors connected]

> "Inside the group you can see three processors connected in a chain.
> This is the full pipeline — from the database, all the way to a saved file on disk.
> Let me walk through each one."

---

## [Click on GenerateTableFetch]

> "The first processor is **GenerateTableFetch**.
> This connects to our MySQL database — `techreads_db` — and automatically generates the SQL
> needed to fetch rows from the `techreads_books` table.
> It's partitioned by the `id` column so it can handle large datasets efficiently by fetching in batches."

---

## [Click on ExecuteSQLRecord]

> "That SQL gets passed down to **ExecuteSQLRecord**.
> This processor actually runs the query against the database and converts the results straight into JSON
> using the `JsonRecordSetWriter` controller service I configured.
> So at this point, structured JSON is flowing through the pipeline."

---

## [Click on PutFile]

> "Finally the JSON flows into **PutFile**.
> This saves the output automatically to a local folder on my machine.
> Every time the pipeline runs, a fresh file gets dropped there — no manual work needed at all."

---

## [Show Controller Services — open the gear/settings icon]

> "I also want to quickly show the controller services.
> Here you can see the `DBCPConnectionPool` is enabled — this is what handles the MySQL connection,
> storing the JDBC URL, username and password securely.
> And here's the `JsonRecordSetWriter` which handles the JSON output format."

---

## [Right-click → Start all processors]

> "Now let me start the flow to show it actually running."

*(Start all processors — wait a moment)*

> "You can see the processors turn green and data starts queuing and moving through the system.
> Each connection shows the FlowFiles passing between processors successfully."

---

## [Open the output folder in File Explorer]

> "And if I open the local output folder now..."

*(Open the nifi_output folder)*

> "You can see the JSON file has been automatically created right here.
> Let me open it to confirm the data looks correct."

*(Open the file)*

> "There we go — you can see the book records in JSON format: titles, prices, ratings — all the fields
> we originally scraped and stored in MySQL are now in this file, delivered automatically."

---

## [Back to camera — wrap up]

> "So that's the Task 3 NiFi pipeline.
> The key advantage over running Python scripts manually is automation — NiFi can run this on a schedule,
> retry if something fails, and scale up without touching any code.
> That's what makes it a proper production-style data engineering tool.
> My name is Sukhjeet Singh Sekhon — thanks for watching."

---

## Delivery Tips

- **Speak slowly and clearly** — you know the content, don't rush it
- **Point at the screen** when you name each processor
- **Pause after each processor section** before moving to the next
- **Camera ON** for intro and outro — face the camera, not the screen
- It does not need to be word-perfect — natural is better than robotic
