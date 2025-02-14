
import { Button } from "@/components/ui/button";
import { Switch } from "@/components/ui/switch";
import { Label } from "@/components/ui/label";
import { useState, useEffect } from "react";
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
} from "@/components/ui/alert-dialog";
import { Input } from "@/components/ui/input";
import { useToast } from "@/components/ui/use-toast";

const Settings = () => {
  const [darkMode, setDarkMode] = useState(false);
  const [resetConfirmation, setResetConfirmation] = useState("");
  const { toast } = useToast();

  useEffect(() => {
    // Check if dark mode is already enabled
    if (document.documentElement.classList.contains("dark")) {
      setDarkMode(true);
    }
  }, []);

  const handleDarkModeToggle = (checked: boolean) => {
    setDarkMode(checked);
    if (checked) {
      document.documentElement.classList.add("dark");
    } else {
      document.documentElement.classList.remove("dark");
    }
    toast({
      title: `${checked ? "Dark" : "Light"} mode enabled`,
      duration: 2000,
    });
  };

  const handleReset = () => {
    if (resetConfirmation.toLowerCase() === "reset me") {
      toast({
        title: "History reset",
        description: "Your learning history has been reset.",
        duration: 3000,
      });
    }
  };

  return (
    <div className="space-y-8">
      <div>
        <h1 className="text-3xl font-bold tracking-tight bg-gradient-to-r from-primary to-primary/70 bg-clip-text text-transparent">
          Settings
        </h1>
        <p className="text-muted-foreground">Manage your preferences</p>
      </div>

      <div className="space-y-6">
        <div className="flex items-center space-x-4">
          <Switch
            id="dark-mode"
            checked={darkMode}
            onCheckedChange={handleDarkModeToggle}
          />
          <Label htmlFor="dark-mode">Dark Mode</Label>
        </div>

        <div className="pt-4">
          <AlertDialog>
            <AlertDialogTrigger asChild>
              <Button variant="destructive">Reset History</Button>
            </AlertDialogTrigger>
            <AlertDialogContent>
              <AlertDialogHeader>
                <AlertDialogTitle>Are you absolutely sure?</AlertDialogTitle>
                <AlertDialogDescription>
                  This action cannot be undone. This will permanently delete your
                  learning history and reset all progress.
                  <div className="mt-4">
                    <Label htmlFor="confirmation">
                      Type "reset me" to confirm:
                    </Label>
                    <Input
                      id="confirmation"
                      value={resetConfirmation}
                      onChange={(e) => setResetConfirmation(e.target.value)}
                      className="mt-2"
                    />
                  </div>
                </AlertDialogDescription>
              </AlertDialogHeader>
              <AlertDialogFooter>
                <AlertDialogCancel>Cancel</AlertDialogCancel>
                <AlertDialogAction
                  onClick={handleReset}
                  disabled={resetConfirmation.toLowerCase() !== "reset me"}
                >
                  Reset
                </AlertDialogAction>
              </AlertDialogFooter>
            </AlertDialogContent>
          </AlertDialog>
        </div>
      </div>
    </div>
  );
};

export default Settings;
