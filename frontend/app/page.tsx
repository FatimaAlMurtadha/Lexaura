"use client";

import { useState } from "react";
import QueryPage from "../components/QueryPage";
import UploadPDF from "../components/UploadPDF";

export default function Home() {
  const [showUpload, setShowUpload] = useState(false);
  const [showQuery, setShowQuery] = useState(false);

  return (
    <div>
      <main className="home-container">
        <div className="home-header">
          <h1 className="home-title">LEXAURA</h1>
          <p className="home-description">Welcome to LEXAURA! Your AI-powered student assistant.</p>

          {!showUpload && (
            <button onClick={() => setShowUpload(true)}
            className="upload-button">
              Would you like to upload a PDF file?
            </button>
          )}
        </div>

        {showUpload && (
          <div className="upload-section">
            <UploadPDF onUploaded={() => setShowQuery(true)} />
          </div>
        )}
        {showQuery && (
          <div className="query-section">
            <QueryPage />
          </div>
        )}
      </main>
    </div>
  );
}
