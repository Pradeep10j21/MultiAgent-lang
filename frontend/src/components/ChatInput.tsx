import type { ChatInputProps } from "../types/chat";

export default function ChatInput({ onSubmit, inputHandler, inputMessage }: ChatInputProps) {
  return (
    <form className="bg-white/10 border border-white/20 shadow-lg text-white w-4/5 mx-auto flex rounded-full p-4 ps-6 mt-4" onSubmit={(e) => {onSubmit(e)}}>
        <input className="flex-1 outline-none focus:ring-0 focus:border-transparent" value={inputMessage} onChange={(e) => inputHandler(e.target.value)} placeholder="Start a research about a company stock"></input>
        <button type="submit" className="cursor-pointer">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="size-6">
                <path strokeLinecap="round" strokeLinejoin="round" d="M6 12 3.269 3.125A59.769 59.769 0 0 1 21.485 12 59.768 59.768 0 0 1 3.27 20.875L5.999 12Zm0 0h7.5" />
            </svg>
        </button>
    </form>
  )
}
