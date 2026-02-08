-- Uber Analytics - Key Business Questions

-- 1. Hourly Booking Volume (Peak Identification)
SELECT 
    strftime('%H', Time) as Hour,
    COUNT(*) as Total_Bookings
FROM bookings
GROUP BY 1
ORDER BY 2 DESC;

-- 2. Vehicle Performance (Completion Rate)
SELECT 
    "Vehicle Type",
    ROUND(SUM(CASE WHEN "Booking Status" = 'Completed' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as Completion_Rate,
    ROUND(AVG("Booking Value"), 2) as Avg_Revenue
FROM bookings
GROUP BY 1
ORDER BY 2 DESC;

-- 3. Top Cancellation Reasons (Supply vs Demand Issue)
SELECT 
    "Reason for cancelling by Customer",
    COUNT(*) as Count
FROM bookings
WHERE "Booking Status" = 'Cancelled by Customer'
GROUP BY 1
ORDER BY 2 DESC
LIMIT 5;

-- 4. High Value Routes (Top Pickup Locations by Revenue)
SELECT 
    "Pickup Location",
    SUM("Booking Value") as Total_Revenue,
    COUNT(*) as Ride_Count
FROM bookings
WHERE "Booking Status" = 'Completed'
GROUP BY 1
ORDER BY 2 DESC
LIMIT 10;
