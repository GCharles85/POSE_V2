using Microsoft.EntityFrameworkCore;
using Diagnoses.Models;

public class DiagnosticContext : DbContext
{
    public DiagnosticContext(DbContextOptions<DiagnosticContext> options)
        : base(options)
    {
    }

    public DbSet<DiagnosticItem> Diagnostics { get; set; }
}
