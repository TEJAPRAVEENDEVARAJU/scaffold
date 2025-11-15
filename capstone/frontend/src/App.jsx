import React, {useState} from "react";

export default function App() {
  const [query, setQuery] = useState("Frontend Developer");
  const [name, setName] = useState("Teja Praveen");
  const [skills, setSkills] = useState("React,JavaScript,HTML,CSS");
  const [status, setStatus] = useState(null);

  async function run() {
    const body = { query, user_profile: {name, skills: skills.split(",")}, max_results: 6 };
    setStatus("Starting...");
    const res = await fetch("http://localhost:8000/run", {
      method: "POST", headers: {"Content-Type":"application/json"}, body: JSON.stringify(body)
    });
    const data = await res.json();
    setStatus(JSON.stringify(data));
  }

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold">AutoApply — Demo UI</h1>
      <div className="mt-4">
        <label>Query:</label>
        <input value={query} onChange={e=>setQuery(e.target.value)} className="border p-2 ml-2" />
      </div>
      <div className="mt-4">
        <label>Name:</label>
        <input value={name} onChange={e=>setName(e.target.value)} className="border p-2 ml-2" />
      </div>
      <div className="mt-4">
        <label>Skills (csv):</label>
        <input value={skills} onChange={e=>setSkills(e.target.value)} className="border p-2 ml-2" />
      </div>
      <button onClick={run} className="mt-4 bg-blue-600 text-white px-4 py-2 rounded">Run AutoApply</button>
      <pre className="mt-4">{status}</pre>
    </div>
  );
}
