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
    <div >
      <h2>Ask a Question</h2>

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
        <pre>
          {answer}
        </pre>
      )}
    </div>
  );
}