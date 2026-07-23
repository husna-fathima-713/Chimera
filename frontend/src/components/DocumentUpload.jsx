import { useState } from "react";
import { uploadDocument } from "../services/documentService";

function DocumentUpload() {

    const [file, setFile] = useState(null);

    async function handleUpload() {

        if (!file) return;

        try {

            const result = await uploadDocument(file);

            alert(result.message);

        } catch (error) {

            console.error(error);

            alert("Upload failed.");

        }

    }

    return (

        <div>

            <input
                type="file"
                onChange={(e) => setFile(e.target.files[0])}
            />

            <button onClick={handleUpload}>
                Upload
            </button>

        </div>

    );
}

export default DocumentUpload;