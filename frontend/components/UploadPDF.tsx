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
    <div className="upload-box">
      <h2 className="upload-title">Upload PDF</h2>

      <form onSubmit={handleUpload} className="upload-form">
        <input type="file" name="file" className="upload-input" />
        <button type="submit" className="upload-btn">
          Upload
        </button>
      </form>

      {result &&
        <pre className="upload-result" >{result}</pre>}
    </div>
  );
}
