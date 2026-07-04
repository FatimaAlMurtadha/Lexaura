import QueryPage from "../components/QueryBox";
import UploadPDF from "../components/UploadPDF";

export default function Home() {
  return (
    <div>
      <main>
        <h1>LEXAURA</h1>
        <UploadPDF />
        <QueryPage/>
      </main>
    </div>
  );
}