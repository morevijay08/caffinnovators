export interface AssistantMessage { role: "user" | "assistant"; content: string }
export interface AssistantReply { answer: string; model: string; disclaimer: string }
