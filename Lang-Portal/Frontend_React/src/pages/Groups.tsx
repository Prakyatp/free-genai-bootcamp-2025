
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { Link } from "react-router-dom";

const groups = [
  {
    id: 1,
    name: "Basic Greetings",
    wordCount: 3,
  },
  {
    id: 2,
    name: "Common Verbs",
    wordCount: 4,
  },
  {
    id: 3,
    name: "Family Members",
    wordCount: 4,
  },
  {
    id: 4,
    name: "Numbers",
    wordCount: 4,
  },
  {
    id: 5,
    name: "Food Items",
    wordCount: 4,
  },
  {
    id: 6,
    name: "Common Phrases",
    wordCount: 15,
  },
];

const Groups = () => {
  return (
    <div className="space-y-8">
      <div>
        <h1 className="text-3xl font-bold tracking-tight bg-gradient-to-r from-primary to-primary/70 bg-clip-text text-transparent">
          Word Groups
        </h1>
        <p className="text-muted-foreground">
          Organize and study words by categories
        </p>
      </div>

      <div className="table-container">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>Group Name</TableHead>
              <TableHead className="text-right"># Words</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {groups.map((group) => (
              <TableRow key={group.id}>
                <TableCell>
                  <Link
                    to={`/groups/${group.id}`}
                    className="font-medium hover:text-primary transition-colors"
                  >
                    {group.name}
                  </Link>
                </TableCell>
                <TableCell className="text-right">{group.wordCount}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </div>
    </div>
  );
};

export default Groups;
