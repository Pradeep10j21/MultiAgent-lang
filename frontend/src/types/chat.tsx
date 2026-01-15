export type Role = "user" | "ai";

export interface ChatMessage {
    role: Role
    message: string
}

export interface ChatInputProps {
  onSubmit: () => void;
  inputHandler: (value: string) => void
  inputMessage: string
}

export interface ChatListProps {
  chat: ChatMessage[]
}
