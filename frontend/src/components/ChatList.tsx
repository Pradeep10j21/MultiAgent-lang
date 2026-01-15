import type { ChatListProps } from "../types/chat";
import ReactMarkdown from 'react-markdown';
import remarkGfm from "remark-gfm";

export default function ChatList({ chat }: ChatListProps){
    return(
        <div className="space-y-6 text-white">
            {chat.map((msg, idx) => {
                if (msg.role === 'user')
                    return <div key={idx} className="bg-white/10 border border-white/20 shadow-lg w-2/3 ml-auto rounded-xl py-2 px-4">{msg.message}</div>
                return <ReactMarkdown key={idx} remarkPlugins={[remarkGfm]}>{msg.message}</ReactMarkdown>
            })}
        </div>
    )
}