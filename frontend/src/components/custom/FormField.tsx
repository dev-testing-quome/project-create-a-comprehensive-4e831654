
import React from 'react';
import { useController, Control } from 'react-hook-form';

interface FormFieldProps {
  name: string;
  control: Control<any>;
  label?: string;
  placeholder?: string;
  type?: 'text' | 'email' | 'password' | 'number' | 'tel' | 'url';
  required?: boolean;
  className?: string;
}

export default function FormField({
  name,
  control,
  label,
  placeholder,
  type = 'text',
  required = false,
  className = '',
}: FormFieldProps) {
  const {
    field,
    fieldState: { error },
  } = useController({
    name,
    control,
    rules: { required: required ? `${label || name} is required` : false },
  });

  return (
    <div className={`space-y-2 ${className}`}>
      {label && (
        <label htmlFor={name} className="text-sm font-medium">
          {label}
          {required && <span className="text-red-500 ml-1">*</span>}
        </label>
      )}
      <input
        {...field}
        id={name}
        type={type}
        placeholder={placeholder}
        className={`w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 ${
          error ? 'border-red-500' : 'border-gray-300'
        }`}
      />
      {error && (
        <p className="text-sm text-red-500">{error.message}</p>
      )}
    </div>
  );
}
