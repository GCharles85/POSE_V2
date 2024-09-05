using Microsoft.EntityFrameworkCore;
using Diagnoses.Models;

namespace Diagnoses.Context;

public class DiagnosticContext : DbContext
{
    public DiagnosticContext(DbContextOptions<DiagnosticContext> options)
        : base(options)
    {
    }

    public DbSet<DiagnosticItem> Diagnostics { get; set; }
}
