import { Geist, Geist_Mono } from "next/font/google";


import "./globals.css";
import { Navbar } from "./_components/Navbar";
import Loader from "./_components/Loader";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata = {
  title: "Brain Deep Analtsis",
  description: "",
};

export default function RootLayout({ children }) {
  return (
    <html lang="pt-br">
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased px-10`}
      >
        <Navbar />
        <Loader/>
        {children}
      </body>
    </html>
  );
}
