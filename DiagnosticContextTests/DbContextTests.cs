using System;
using Xunit;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.EntityFrameworkCore;
using Diagnoses.Context; // replace with your actual namespace

public class DbContextTests
{
    [Fact]
    public void TestDbContextConnectionString()
    {
        // Arrange
        var services = new ServiceCollection();
        
        // Set the environment variable
        //Environment.SetEnvironmentVariable("CONNECTION_STRING", "Server=myServer;Database=myDB;User=myUser;Password=myPass;");

        // Act
        services.AddDbContext<DiagnosticContext>(options =>
            options.UseSqlServer(Environment.GetEnvironmentVariable("CONNECTION_STRING")));

        // Build service provider
        var serviceProvider = services.BuildServiceProvider();

        // Assert
        var context = serviceProvider.GetService<DiagnosticContext>();
        Assert.NotNull(context); // Check if the context was created successfully
    }

    
}


    