
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { CircleCheck, BookText, Book } from "lucide-react";

const Dashboard = () => {
  // Simulated data - this would come from your backend in a real app
  const stats = {
    totalWords: 120,
    successRate: 85,
    lastSession: "No sessions yet",
  };

  return (
    <div className="space-y-8">
      <div>
        <h1 className="text-3xl font-bold tracking-tight bg-gradient-to-r from-primary to-primary/70 bg-clip-text text-transparent">Dashboard</h1>
        <p className="text-muted-foreground">
          Welcome to your Kannada learning journey
        </p>
      </div>

      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
        <Card className="border-none shadow-md bg-gradient-to-br from-card to-card/50 backdrop-blur-sm">
          <CardHeader className="flex flex-row items-center justify-between pb-2 space-y-0">
            <CardTitle className="text-sm font-medium">Total Words</CardTitle>
            <BookText className="h-4 w-4 text-muted-foreground" />
          </CardHeader>
          <CardContent>
            <p className="text-2xl font-bold">{stats.totalWords}</p>
            <p className="text-xs text-muted-foreground">Words in your library</p>
          </CardContent>
        </Card>

        <Card className="border-none shadow-md bg-gradient-to-br from-card to-card/50 backdrop-blur-sm">
          <CardHeader className="flex flex-row items-center justify-between pb-2 space-y-0">
            <CardTitle className="text-sm font-medium">Success Rate</CardTitle>
            <CircleCheck className="h-4 w-4 text-muted-foreground" />
          </CardHeader>
          <CardContent>
            <p className="text-2xl font-bold">{stats.successRate}%</p>
            <p className="text-xs text-muted-foreground">Average success rate</p>
          </CardContent>
        </Card>

        <Card className="border-none shadow-md bg-gradient-to-br from-card to-card/50 backdrop-blur-sm">
          <CardHeader className="flex flex-row items-center justify-between pb-2 space-y-0">
            <CardTitle className="text-sm font-medium">Last Session</CardTitle>
            <Book className="h-4 w-4 text-muted-foreground" />
          </CardHeader>
          <CardContent>
            <p className="text-2xl font-bold">{stats.lastSession}</p>
            <p className="text-xs text-muted-foreground">Start a study activity to begin learning</p>
          </CardContent>
        </Card>
      </div>
    </div>
  );
};

export default Dashboard;
