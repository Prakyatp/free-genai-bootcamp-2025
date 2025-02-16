
import { Card, CardHeader, CardTitle, CardDescription, CardContent, CardFooter } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Link } from "react-router-dom";
import { Library, ArrowUpRightFromSquare, ChevronRight } from "lucide-react";

const activities = [
  {
    id: 1,
    title: "Flashcards",
    description: "Learn Kannada words through interactive flashcards with spaced repetition.",
    icon: Library,
    launchUrl: "http://localhost:8081?group_id=4", // This would be your actual flashcards app URL
  },
];

const StudyActivities = () => {
  const handleLaunch = (url: string) => {
    window.open(url, "_blank");
  };

  return (
    <div className="space-y-8">
      <div>
        <h1 className="text-3xl font-bold tracking-tight bg-gradient-to-r from-primary to-primary/70 bg-clip-text text-transparent">
          Study Activities
        </h1>
        <p className="text-muted-foreground">
          Choose an activity to start learning
        </p>
      </div>

      <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
        {activities.map((activity) => (
          <Card key={activity.id} className="border-none shadow-md bg-gradient-to-br from-card to-card/50 backdrop-blur-sm">
            <CardHeader>
              <div className="flex items-center justify-between">
                <activity.icon className="h-8 w-8 text-primary" />
                <Button
                  variant="ghost"
                  size="icon"
                  onClick={() => handleLaunch(activity.launchUrl)}
                >
                  <ArrowUpRightFromSquare className="h-4 w-4" />
                </Button>
              </div>
              <CardTitle className="text-xl">{activity.title}</CardTitle>
              <CardDescription>{activity.description}</CardDescription>
            </CardHeader>
            <CardFooter className="justify-between">
              <Link
                to={`/study-activities/${activity.id}`}
                className="inline-flex items-center text-sm text-muted-foreground hover:text-primary transition-colors"
              >
                View Details
                <ChevronRight className="ml-1 h-4 w-4" />
              </Link>
              <Button onClick={() => handleLaunch(activity.launchUrl)}>
                Launch
              </Button>
            </CardFooter>
          </Card>
        ))}
      </div>
    </div>
  );
};

export default StudyActivities;
