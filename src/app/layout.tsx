import type { Metadata, Viewport } from "next";
import { Figtree, Syne } from "next/font/google";
import "./globals.css";

const body = Figtree({
  variable: "--font-body",
  subsets: ["latin"],
});

const display = Syne({
  variable: "--font-display",
  subsets: ["latin"],
});

const siteUrl = new URL("https://kelvinwieth.github.io/perfil7/");

export const metadata: Metadata = {
  metadataBase: siteUrl,
  title: "Perfil 7 · Cartas novas",
  description:
    "Baralho digital de cartas novas do Perfil 7 para ler no celular, com tabuleiro físico.",
  applicationName: "Perfil 7 Cartas",
  appleWebApp: {
    capable: true,
    title: "Perfil 7",
    statusBarStyle: "black-translucent",
  },
  icons: {
    icon: [{ url: "icon.svg", type: "image/svg+xml" }],
    apple: [{ url: "apple-icon.svg", type: "image/svg+xml" }],
  },
};

export const viewport: Viewport = {
  width: "device-width",
  initialScale: 1,
  viewportFit: "cover",
  themeColor: "#1a0d2e",
};

export default function RootLayout({ children }: LayoutProps<"/">) {
  return (
    <html
      lang="pt-BR"
      className={`${body.variable} ${display.variable} h-full antialiased`}
    >
      <body className="min-h-full flex flex-col">{children}</body>
    </html>
  );
}
