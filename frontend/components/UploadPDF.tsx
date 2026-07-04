"use client";

import { useState } from "react";
import { uploadPDF } from "@/lib/api";

export default function UploadPDF() {
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
    <div>
      <h2>Upload PDF</h2>

      <form onSubmit={handleUpload}>
        <input type="file" name="file" />
        <button type="submit">Upload</button>
      </form>

      {result && (
        <pre>
          {result}
        </pre>
      )}
    </div>
  );
}