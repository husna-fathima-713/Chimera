import api from "../api/api";

export async function uploadDocument(file) {

    const formData = new FormData();

    formData.append("file", file);

    const response = await api.post(
        "/documents",
        formData,
        {
            headers: {
                "Content-Type": "multipart/form-data",
            },
        }
    );

    return response.data;
}