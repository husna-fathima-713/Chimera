const API_URL = "http://127.0.0.1:8000";

export async function sendMessage(chatId, prompt, onChunk) {

    const response = await fetch(

        `${API_URL}/chat`,

        {

            method: "POST",

            headers: {

                "Content-Type": "application/json",

            },

            body: JSON.stringify({

                chat_id: chatId,

                prompt: prompt,

            }),

        }

    );

    if (!response.ok) {

        throw new Error("Failed to contact backend.");

    }

    const reader = response.body.getReader();

    const decoder = new TextDecoder();

    let fullResponse = "";

    while (true) {

        const { done, value } = await reader.read();

        if (done) {

            break;

        }

        const chunk = decoder.decode(value);

        fullResponse += chunk;

        if (onChunk) {

            onChunk(fullResponse);

        }

    }

    return fullResponse;

}