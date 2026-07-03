"use client";

import { useState } from "react";
import { queryDocument } from "@/lib/api";

export default function QueryPage() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  async function handleAsk(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    const res = await queryDocument(question);
    setAnswer(JSON.stringify(res, null, 2));
  }

  return (
    <div style={{ padding: "20px" }}>
      <h1>Ask a Question</h1>

      <form onSubmit={handleAsk}>
        <input
          type="text"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Enter your question..."
        />
        <button type="submit">Ask</button>
      </form>

      {answer && (
        <pre style={{ marginTop: "20px", background: "#eee", padding: "10px" }}>
          {answer}
        </pre>
      )}
    </div>
  );
}