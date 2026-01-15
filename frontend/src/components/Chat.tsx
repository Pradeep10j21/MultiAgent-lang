import { useEffect, useRef, useState } from "react";
import ChatInput from "./ChatInput";
import type { ChatMessage } from "../types/chat";
import ChatList from "./ChatList";

export default function Chat() {
  const [inputMessage, setInputMessage] = useState("");
  const [chat, setChat] = useState<ChatMessage[]>([]);

  const apiUrl = import.meta.env.VITE_API_URL;

  // for auto scroll
  const bottomRef = useRef<HTMLDivElement | null>(null);
  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [chat]);

  // Singleton event source for stream
  const eventSourceRef = useRef<EventSource | null>(null);

  // sending prompt
  const handleSend = (): void => {
    if (!inputMessage.trim()) return;

    // 1. Add user message
    setChat((prev) => [
      ...prev,
      { role: "user", message: inputMessage },
      { role: "ai", message: "" }, // placeholder for streaming
    ]);

    // 2. Close any existing stream
    eventSourceRef.current?.close();

    // 3. Open new SSE stream
    const es = new EventSource(
      `${apiUrl}/chat/${"212113"}?prompt=${encodeURIComponent(inputMessage)}`
    );

    // 4. Receive streamed tokens
    es.onmessage = (event) => {
      const data = JSON.parse(event.data);

      if (data.type === "approval_required" || data.type === "stream_end") {
        es.close();
        eventSourceRef.current = null;
        return;
      }

      if (data.type === "token") {
        setChat((prev) => {
          const next = [...prev];
          next[next.length - 1] = {
            ...next[next.length - 1],
            message: next[next.length - 1].message + data.content,
          };
          return next;
        });
      }
    };

    es.onerror = () => {
      es.close();
      eventSourceRef.current = null;
    };

    setInputMessage("");
  };
  const updateInput = (value: string) => setInputMessage(value);

  return (
    <div className="h-screen flex-1 flex flex-col p-5">
      <div className="flex-1 min-h-0 overflow-y-auto">
        <ChatList chat={chat} />
        <div ref={bottomRef} />
      </div>

      <ChatInput
        onSubmit={handleSend}
        inputHandler={updateInput}
        inputMessage={inputMessage}
      />
    </div>
  );
}
