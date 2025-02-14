
import { Outlet, useLocation, Link } from "react-router-dom";
import { cn } from "@/lib/utils";

const navigation = [
  { name: "Dashboard", href: "/dashboard" },
  { name: "Study Activities", href: "/study-activities" },
  { name: "Words", href: "/words" },
  { name: "Word Groups", href: "/groups" },
  { name: "Sessions", href: "/sessions" },
  { name: "Settings", href: "/settings" },
];

const Layout = () => {
  const location = useLocation();
  const pathSegments = location.pathname.split("/").filter(Boolean);

  return (
    <div className="min-h-screen">
      <header className="border-b bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
        <nav className="container mx-auto px-4">
          <div className="flex h-16 items-center justify-between">
            <div className="flex flex-1 items-center justify-start">
              {navigation.map((item) => (
                <Link
                  key={item.name}
                  to={item.href}
                  className={cn(
                    "nav-link",
                    location.pathname === item.href && "nav-link-active"
                  )}
                >
                  {item.name}
                </Link>
              ))}
            </div>
          </div>
        </nav>
      </header>

      <div className="container mx-auto px-4">
        <nav className="flex py-4" aria-label="Breadcrumb">
          <ol className="flex items-center space-x-2">
            {pathSegments.map((segment, index) => {
              const path = `/${pathSegments.slice(0, index + 1).join("/")}`;
              const isLast = index === pathSegments.length - 1;

              return (
                <li key={path} className="flex items-center">
                  {index > 0 && (
                    <span className="mx-2 text-muted-foreground">/</span>
                  )}
                  <Link
                    to={path}
                    className={cn(
                      "text-sm transition-colors hover:text-primary",
                      isLast
                        ? "font-medium text-foreground"
                        : "text-muted-foreground"
                    )}
                  >
                    {segment.charAt(0).toUpperCase() + segment.slice(1)}
                  </Link>
                </li>
              );
            })}
          </ol>
        </nav>
      </div>

      <main className="page-container">
        <Outlet />
      </main>
    </div>
  );
};

export default Layout;
