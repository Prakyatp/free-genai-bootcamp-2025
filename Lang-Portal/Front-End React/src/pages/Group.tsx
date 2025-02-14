import { useParams } from "react-router-dom";
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

// Sample data - in a real app, this would come from your backend
const groupData = {
  1: {
    name: "Basic Greetings",
    words: [
      { id: 1, kannada: "ನಮಸ್ಕಾರ", english: "Hello" },
      { id: 2, kannada: "ಧನ್ಯವಾದ", english: "Thank you" },
      { id: 3, kannada: "ಹೇಗಿದ್ದೀರಾ", english: "How are you" },
    ]
  },
  2: {
    name: "Common Verbs",
    words: [
      { id: 1, kannada: "ಹೋಗು", english: "Go" },
      { id: 2, kannada: "ಬಾ", english: "Come" },
      { id: 3, kannada: "ಮಾಡು", english: "Do" },
      { id: 4, kannada: "ತಿನ್ನು", english: "Eat" },
    ]
  },
  3: {
    name: "Family Members",
    words: [
      { id: 1, kannada: "ಅಮ್ಮ", english: "Mother" },
      { id: 2, kannada: "ಅಪ್ಪ", english: "Father" },
      { id: 3, kannada: "ಅಣ್ಣ", english: "Elder Brother" },
      { id: 4, kannada: "ತಂಗಿ", english: "Younger Sister" },
    ]
  },
  4: {
    name: "Numbers",
    words: [
      { id: 1, kannada: "ಒಂದು", english: "One" },
      { id: 2, kannada: "ಎರಡು", english: "Two" },
      { id: 3, kannada: "ಮೂರು", english: "Three" },
      { id: 4, kannada: "ನಾಲ್ಕು", english: "Four" },
    ]
  },
  5: {
    name: "Food Items",
    words: [
      { id: 1, kannada: "ಅನ್ನ", english: "Rice" },
      { id: 2, kannada: "ಹಣ್ಣು", english: "Fruit" },
      { id: 3, kannada: "ಹಾಲು", english: "Milk" },
      { id: 4, kannada: "ನೀರು", english: "Water" },
    ]
  },
  6: {
    name: "Common Phrases",
    words: [
      { id: 1, kannada: "ನಿಮ್ಮ ಹೆಸರೇನು?", english: "What is your name?" },
      { id: 2, kannada: "ನನ್ನ ಹೆಸರು...", english: "My name is..." },
      { id: 3, kannada: "ನಾನು ಕನ್ನಡ ಕಲಿಯುತ್ತಿದ್ದೇನೆ", english: "I am learning Kannada" },
      { id: 4, kannada: "ನನಗೆ ಅರ್ಥವಾಗಲಿಲ್ಲ", english: "I don't understand" },
      { id: 5, kannada: "ದಯವಿಟ್ಟು ನಿಧಾನವಾಗಿ ಮಾತನಾಡಿ", english: "Please speak slowly" },
      { id: 6, kannada: "ಸ್ವಲ್ಪ ನೀರು ಕೊಡ್ತೀರಾ?", english: "Can you give me some water?" },
      { id: 7, kannada: "ಊಟ ಆಯ್ತಾ?", english: "Have you had food?" },
      { id: 8, kannada: "ನಾನು ಭಾರತದಿಂದ", english: "I am from India" },
      { id: 9, kannada: "ನಿಮಗೆ ಕನ್ನಡ ಬರುತ್ತಾ?", english: "Do you know Kannada?" },
      { id: 10, kannada: "ಇದು ಎಷ್ಟು?", english: "How much is this?" },
      { id: 11, kannada: "ನನಗೆ ಕನ್ನಡ ಇಷ್ಟ", english: "I like Kannada" },
      { id: 12, kannada: "ಸಿಹಿ ತಿನ್ನಿ", english: "Have some sweets" },
      { id: 13, kannada: "ಮತ್ತೆ ಸಿಗೋಣ", english: "See you again" },
      { id: 14, kannada: "ಶುಭ ರಾತ್ರಿ", english: "Good night" },
      { id: 15, kannada: "ಶುಭೋದಯ", english: "Good morning" }
    ]
  }
} as const;

type GroupId = keyof typeof groupData;

const Group = () => {
  const { id } = useParams();
  const groupId = id ? parseInt(id) as GroupId : null;
  const group = groupId ? groupData[groupId] : null;

  const playSound = (word: string) => {
    // This would integrate with a text-to-speech service in a real app
    console.log(`Playing sound for: ${word}`);
  };

  if (!group) {
    return (
      <div className="space-y-8">
        <div>
          <h1 className="text-3xl font-bold tracking-tight bg-gradient-to-r from-primary to-primary/70 bg-clip-text text-transparent">
            Group Not Found
          </h1>
        </div>
      </div>
    );
  }

  return (
    <div className="space-y-8">
      <div>
        <h1 className="text-3xl font-bold tracking-tight bg-gradient-to-r from-primary to-primary/70 bg-clip-text text-transparent">
          {group.name}
        </h1>
        <p className="text-muted-foreground">
          Learn words in this category
        </p>
      </div>

      <div className="table-container">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>Kannada</TableHead>
              <TableHead>English</TableHead>
              <TableHead className="w-[100px]">Listen</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {group.words.map((word) => (
              <TableRow key={word.id}>
                <TableCell className="font-medium">
                  {word.kannada}
                </TableCell>
                <TableCell>{word.english}</TableCell>
                <TableCell>
                  <Button
                    variant="ghost"
                    size="sm"
                    className="h-8 w-8 p-0"
                    onClick={() => playSound(word.kannada)}
                  >
                    <Volume2 className="h-4 w-4" />
                  </Button>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </div>
    </div>
  );
};

export default Group;
