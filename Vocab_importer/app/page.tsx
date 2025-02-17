"use client"

import type React from "react"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Textarea } from "@/components/ui/textarea"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { AlertCircle, Copy, BookOpen } from "lucide-react"
import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert"

export default function VocabImporter() {
  const [theme, setTheme] = useState("")
  const [jsonOutput, setJsonOutput] = useState("")
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState("")
  const [copied, setCopied] = useState(false)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setIsLoading(true)
    setError("")
    setJsonOutput("")

    try {
      const response = await fetch("/api/generate-vocab", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ theme }),
      })

      if (!response.ok) {
        throw new Error("Failed to generate vocabulary")
      }

      const data = await response.json()
      setJsonOutput(JSON.stringify(data, null, 2))
    } catch (err) {
      setError("An error occurred while generating the vocabulary.")
    } finally {
      setIsLoading(false)
    }
  }

  const copyToClipboard = () => {
    navigator.clipboard.writeText(jsonOutput)
    setCopied(true)
    setTimeout(() => setCopied(false), 2000)
  }

  return (
    <div className="min-h-screen bg-gradient-to-b from-purple-100 to-white py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-3xl mx-auto">
        <Card className="shadow-xl">
          <CardHeader className="text-center">
            <BookOpen className="w-12 h-12 text-purple-500 mx-auto mb-4" />
            <CardTitle className="text-3xl font-bold text-gray-800">Vocabulary Language Importer</CardTitle>
            <CardDescription className="text-lg text-gray-600">
              Enter a thematic category to generate vocabulary using Groq
            </CardDescription>
          </CardHeader>
          <CardContent>
            <form onSubmit={handleSubmit} className="space-y-6">
              <div>
                <Input
                  placeholder="Enter thematic category (e.g., 'Food', 'Travel')"
                  value={theme}
                  onChange={(e) => setTheme(e.target.value)}
                  required
                  className="text-lg py-3"
                />
              </div>
              <Button
                type="submit"
                disabled={isLoading}
                className="w-full text-lg py-6 bg-purple-500 hover:bg-purple-600"
              >
                {isLoading ? "Generating..." : "Generate Vocabulary"}
              </Button>
            </form>

            {error && (
              <Alert variant="destructive" className="mt-6">
                <AlertCircle className="h-5 w-5" />
                <AlertTitle>Error</AlertTitle>
                <AlertDescription>{error}</AlertDescription>
              </Alert>
            )}

            {jsonOutput && (
              <div className="mt-8 space-y-4">
                <div className="flex justify-between items-center">
                  <h3 className="text-xl font-semibold text-gray-800">Generated Vocabulary:</h3>
                  <Button variant="outline" size="sm" onClick={copyToClipboard} className="flex items-center">
                    <Copy className="h-4 w-4 mr-2" />
                    {copied ? "Copied!" : "Copy to Clipboard"}
                  </Button>
                </div>
                <Textarea value={jsonOutput} readOnly className="font-mono text-sm h-96 bg-gray-50 border-gray-300" />
              </div>
            )}
          </CardContent>
        </Card>
      </div>
    </div>
  )
}

