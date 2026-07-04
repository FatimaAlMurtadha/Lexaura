"use client";

import { useState } from "react";
import { uploadPDF } from "@/lib/api";

type UploadPDFProps = {
  onUploaded?: () => void;
};

export default function UploadPDF({ onUploaded }: UploadPDFProps) {
  const [result, setResult] = useState("");

  async function handleUpload(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    const fileInput = e.currentTarget.file as HTMLInputElement;
    const file = fileInput.files?.[0];
    if (!file) return;

    const res = await uploadPDF(file);
    setResult(JSON.stringify(res, null, 2));
    if (onUploaded) onUploaded();
  }

  return (
    <div>
      <h2>Upload PDF</h2>

      <form onSubmit={handleUpload}>
        <input type="file" name="file" />
        <button type="submit">Upload</button>
      </form>

      {result && <pre>{result}</pre>}
    </div>
  );
}
