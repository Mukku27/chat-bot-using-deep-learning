import React, { useState } from "react";
import axios from "axios";
import { gsap } from "gsap";
import "./App.css"; // Import Tailwind styles here

function App() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");

  const sendMessage = async () => {
    if (message.trim() === "") return;

    try {
      const res = await axios.post("http://localhost:5000/chatbot", { message });
      setResponse(res.data.response);

      // Animation for the chatbot response
      gsap.fromTo(".response", { opacity: 0 }, { opacity: 1, duration: 1 });
    } catch (error) {
      console.error("Error communicating with the backend:", error);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gray-100">
      <h1 className="text-4xl font-bold mb-8">Chatbot Application</h1>
      <div className="w-full max-w-md">
        <input
          type="text"
          className="w-full p-4 text-lg border rounded mb-4"
          placeholder="Type your message..."
          value={message}
          onChange={(e) => setMessage(e.target.value)}
        />
        <button
          className="w-full p-4 bg-blue-500 text-white text-lg rounded"
          onClick={sendMessage}
        >
          Send
        </button>
      </div>
      {response && (
        <div className="response mt-8 p-4 bg-white rounded shadow">
          <p className="text-lg">{response}</p>
        </div>
      )}
    </div>
  );
}

export default App;
