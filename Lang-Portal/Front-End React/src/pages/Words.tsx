
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { Volume2 } from "lucide-react";
import { Button } from "@/components/ui/button";

const words = [
  {
    id: 1,
    kannada: "ನಮಸ್ಕಾರ",
    english: "Hello",
    correct: 15,
    wrong: 3,
  },
  {
    id: 2,
    kannada: "ಧನ್ಯವಾದ",
    english: "Thank you",
    correct: 12,
    wrong: 2,
  },
  {
    id: 3,
    kannada: "ಹೇಗಿದ್ದೀರಾ",
    english: "How are you",
    correct: 8,
    wrong: 4,
  },
  {
    id: 4,
    kannada: "ನಾನು",
    english: "I/Me",
    correct: 20,
    wrong: 1,
  },
  {
    id: 5,
    kannada: "ನೀನು",
    english: "You",
    correct: 18,
    wrong: 2,
  },
];

const Words = () => {
  const playSound = (word: string) => {
    // This would integrate with a text-to-speech service in a real app
    console.log(`Playing sound for: ${word}`);
  };

  return (
    <div className="space-y-8">
      <div>
        <h1 className="text-3xl font-bold tracking-tight bg-gradient-to-r from-primary to-primary/70 bg-clip-text text-transparent">
          Words
        </h1>
        <p className="text-muted-foreground">
          Explore and learn Kannada vocabulary
        </p>
      </div>

      <div className="table-container">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>Kannada</TableHead>
              <TableHead>English</TableHead>
              <TableHead className="text-right"># Correct</TableHead>
              <TableHead className="text-right"># Wrong</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {words.map((word) => (
              <TableRow key={word.id}>
                <TableCell className="font-medium">
                  <div className="flex items-center space-x-2">
                    <span>{word.kannada}</span>
                    <Button
                      variant="ghost"
                      size="sm"
                      className="h-8 w-8 p-0"
                      onClick={() => playSound(word.kannada)}
                    >
                      <Volume2 className="h-4 w-4" />
                    </Button>
                  </div>
                </TableCell>
                <TableCell>{word.english}</TableCell>
                <TableCell className="text-right font-medium text-green-600">
                  {word.correct}
                </TableCell>
                <TableCell className="text-right font-medium text-red-600">
                  {word.wrong}
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </div>
    </div>
  );
};

export default Words;
