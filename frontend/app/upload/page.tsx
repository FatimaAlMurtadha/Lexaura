"use client";

import { useState } from "react";
import { uploadPDF } from "@/lib/api";

export default function UploadPage() {
  const [result, setResult] = useState("");

  async function handleUpload(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    const fileInput = e.currentTarget.file as HTMLInputElement;
    const file = fileInput.files?.[0];
    if (!file) return;

    const res = await uploadPDF(file);
    setResult(JSON.stringify(res, null, 2));
  }

  return (
    <div style={{ padding: "20px" }}>
      <h1>Upload PDF</h1>

      <form onSubmit={handleUpload}>
        <input type="file" name="file" />
        <button type="submit">Upload</button>
      </form>

      {result && (
        <pre style={{ marginTop: "20px", background: "#eee", padding: "10px" }}>
          {result}
        </pre>
      )}
    </div>
  );
}