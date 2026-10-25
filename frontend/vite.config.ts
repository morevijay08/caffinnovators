import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  // Render's production URL is different from localhost. Explicitly allow
  // the public frontend hosts so Vite preview doesn't reject requests by Host.
  preview: {
    host: "0.0.0.0",
    allowedHosts: [
      "caffinnovators-1.onrender.com",
      "caffinnovators.onrender.com",
    ],
  },
  server: {
    host: "0.0.0.0",
    port: 5173,
    strictPort: true,
  },
});
