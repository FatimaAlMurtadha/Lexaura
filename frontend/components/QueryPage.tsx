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
    <div className="query-box">
      <h2 className="query-title">Ask a Question</h2>

      <form onSubmit={handleAsk} className="query-form">
        <input
          type="text"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Enter your question..."
          className="query-input"
        />
        <button type="submit" className="query-btn">
          Ask
        </button>
      </form>

      {answer && (
        <pre className="query-result">
          {answer}
        </pre>
      )}
    </div>
  );
}