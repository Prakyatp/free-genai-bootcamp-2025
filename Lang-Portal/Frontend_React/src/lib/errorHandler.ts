import { toast as sonnerToast } from "sonner";

export const handleApiError = (error: any) => {
  const message = error.response?.data?.message || 'An error occurred';
  sonnerToast.error(message);
  return Promise.reject(error);
};