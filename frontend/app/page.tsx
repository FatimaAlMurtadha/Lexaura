"use client";

import { useState } from "react";
import QueryPage from "../components/QueryPage";
import UploadPDF from "../components/UploadPDF";

export default function Home() {
  const [showUpload, setShowUpload] = useState(false);
  const [showQuery, setShowQuery] = useState(false);

  return (
    <div>
      <main>
        <h1>LEXAURA</h1>
        <p>Welcome to LEXAURA! Your AI-powered student assistant.</p>
        {!showUpload && (
          <button onClick={() => setShowUpload(true)}>
            Would you like to upload a PDF file?
          </button>
        )}
        {showUpload && (
          <div>
            <UploadPDF onUploaded={() => setShowQuery(true)} />
          </div>
        )}
        {showQuery && (
          <div>
            <QueryPage />
          </div>
        )}
      </main>
    </div>
  );
}
